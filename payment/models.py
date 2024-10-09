# payment/models.py

from django.db import models
from django.contrib.auth.models import User


# payment/models.py

from django.db import models
from django.contrib.auth.models import User
from store.models import Product  # Assuming your Product model is in a separate app

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link order to a specific user
    date_ordered = models.DateTimeField(auto_now_add=True)  # Automatically sets the order date
    complete = models.BooleanField(default=False)  # Tracks if the order is complete
    transaction_id = models.CharField(max_length=100, null=True, blank=True)  # Unique transaction ID (optional)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    @property
    def get_cart_total(self):
        """Calculate the total cost of all items in the order."""
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        """Get the total number of items in the order."""
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link each order item to a product
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Each order item belongs to a specific order
    quantity = models.IntegerField(default=1)  # Quantity of the product ordered
    date_added = models.DateTimeField(auto_now_add=True)  # When the item was added to the order

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    @property
    def get_total(self):
        """Calculate the total price for this item (product price * quantity)."""
        return self.product.price * self.quantity


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.address_line_1}, {self.city}, {self.country}'

