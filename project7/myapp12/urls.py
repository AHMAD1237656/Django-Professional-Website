from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('feedback/', views.feedback, name='feedback'),
    path('products/', views.products, name='products'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('place-order/', views.place_order, name='place_order'),

]
