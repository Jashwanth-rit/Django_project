# payment/urls.py

from django.urls import path
from . import views

urlpatterns = [
     path('checkout/', views.checkout_view, name='checkout'),
    path('shipping-address/', views.manage_shipping_address, name='shipping_address'),
    path('payment-success/', views.payment_success, name='payment_success'),  # Assuming this exists
     path('payment-section/', views.payment_section, name='payment_section'),  # Assuming this exists
    path('orders/', views.orders, name='orders'),  # Orders URL
]
