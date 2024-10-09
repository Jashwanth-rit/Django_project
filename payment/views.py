from django.shortcuts import render

# Create your views here.
# payment/views.py
# payment/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ShippingAddress
from .forms import ShippingAddressForm

from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart

from store.models import Product
from .models import ShippingAddress
from .forms import ShippingAddressForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Order, OrderItem  # Import the Order and OrderItem models

@login_required
def checkout_view(req):
    cart = Cart(req)
    cart_items = cart.cart_get()  # Get the cart items
    quantity = cart.get_quants()  # Get product quantities
    quantity_range = range(1, 11)  # Quantity selection range (1 to 10)

    # Check if there's an existing shipping address for the logged-in user
    try:
       # Check if there's an existing shipping address for the logged-in user
        shipping_address = ShippingAddress.objects.filter(user=req.user).first()

    except ShippingAddress.DoesNotExist:
        shipping_address = None

    # Shipping form (auto-filled if an address already exists)
    if req.method == 'POST':
        form = ShippingAddressForm(req.POST, instance=shipping_address)  # Pass the existing address, if any
        if form.is_valid():
            # Save shipping address
            shipping_address = form.save(commit=False)
            shipping_address.user = req.user  # Set the user to the logged-in user
            shipping_address.save()

            # Create the order
            order = Order.objects.create(
                user=req.user,
                complete=True,  # Assuming it's complete after checkout
            )

            # Now set the transaction_id after the order has been created
            order.transaction_id = "TXN" + str(order.id)
            order.save()  # Save the order with the transaction ID

            # Loop through cart items and create OrderItem for each
            for item in cart_items:
                item_quantity = quantity.get(str(item.id), 1)  # Get quantity for the item or default to 1

                OrderItem.objects.create(
                    product=item,
                    order=order,
                    quantity=item_quantity,  # Use the selected quantity
                )

            # Clear the cart after creating the order
            cart.clear()

            # Redirect to success page
            return redirect('payment_success')  # Redirect to payment or success page after form submission
    else:
        form = ShippingAddressForm(instance=shipping_address)  # Pass the existing address to the form

    # Calculate total for each item and overall cart
    cart_total = 0
    for item in cart_items:
        item_quantity = quantity.get(str(item.id), 1)  # Get quantity for the item or default to 1
        
        if item.is_sale:
            item_total = item.sale_price * item_quantity
        else:
            item_total = item.price * item_quantity
        
        cart_total += item_total

    return render(req, 'payment/checkout.html', {
        'cart_items': cart_items,
        'quantity_range': quantity_range,
        'quantity': quantity,
        'cart_total': cart_total,
        'form': form,  # Include the shipping form in the context, pre-filled if address exists
    })


@login_required
def orders(request):
    user_orders = Order.objects.filter(user=request.user)  # Get all orders for the logged-in user

    return render(request, 'payment/orders.html', {
        'orders': user_orders  # Pass the orders to the template
    })



@login_required
def manage_shipping_address(request):
    try:
        # Try to get the existing shipping address for the logged-in user
        # Check if there's an existing shipping address for the logged-in user
        shipping_address = ShippingAddress.objects.filter(user=request.user).first()

    except ShippingAddress.DoesNotExist:
        # If it doesn't exist, we'll create a new one
        shipping_address = None

    if request.method == 'POST':
        if shipping_address:
            # If the address exists, update it
            form = ShippingAddressForm(request.POST, instance=shipping_address)
        else:
            # Create a new address for the user
            form = ShippingAddressForm(request.POST)
        
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user  # Set the user
            address.save()
            return redirect('payment/payment_success')  # Redirect to success page after saving
    else:
        # Prepopulate the form with the user's existing data if available
        form = ShippingAddressForm(instance=shipping_address)

    return render(request, 'payment/shipping_address.html', {'form': form})



def payment_success(request):
    return render(request, 'payment/payment_success.html', {
        'message': 'Payment was successful!',  # You can pass a success message to the template
    })

