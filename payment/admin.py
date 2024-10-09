# payment/admin.py

from django.contrib import admin
from .models import ShippingAddress
# payment/admin.py

from django.contrib import admin
from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)


# Register your models here.
admin.site.register(ShippingAddress)
