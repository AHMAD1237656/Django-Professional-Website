from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Product, Order

# 🛒 Order Placement View
def place_order(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        product = request.POST['product']
        quantity = request.POST['quantity']
        message = request.POST.get('message', '')

        # ✅ Save order to database
        Order.objects.create(
            name=name,
            email=email,
            product=product,
            quantity=quantity,
            message=message
        )

        # ✅ Send confirmation email to user
        send_mail(
            "🛍️ Order Confirmation",
            f"Dear {name},\n\nThank you for your order of {quantity} x {product}. We'll be in touch soon!",
            settings.DEFAULT_FROM_EMAIL,
            [email]
        )

        send_mail(
            f"🛒 New Order from {name}",
            f"Product: {product}\nQuantity: {quantity}\nEmail: {email}\nMessage: {message}",
            settings.DEFAULT_FROM_EMAIL,
            ['75ahmadjutt@gmail.com']  # ✅ Replace with your real admin email
        )

        messages.success(request, "✅ Your order has been placed successfully!")
        return redirect('home')

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        # ✅ Send feedback email to admin
        subject = f"💬 New Feedback from {name}"
        message = f"""
        Name: {name}
        Email: {email}
        Rating: {rating}
        Comments: {comments}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['75ahmadjutt@gmail.com']  # ✅ Replace with your real admin email
        )

        messages.success(request, "Thank you for your feedback! 💌")
        return redirect('feedback')
    else:
        return redirect('feedback')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def feedback(request):
    return render(request, 'feedback.html')

# 🛍️ Product Listing Page
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
