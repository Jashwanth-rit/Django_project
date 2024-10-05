from django.shortcuts import redirect, render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_get(req):
    cart = Cart(req)
    cart_items = cart.cart_get()  # Get the cart items
    quantity = cart.get_quants()  # Get product quantities
    quantity_range = range(1, 11)  # Quantity selection range (1 to 10)

    # Calculate total for each item and overall cart
    cart_total = 0
    for item in cart_items:
        item_quantity = quantity.get(str(item.id), 1)  # Get quantity for the item or default to 1
        
        # Check if the item is on sale and calculate the total based on sale price or regular price
        if item.is_sale:
            item_total = item.sale_price * item_quantity  # Use sale price if the item is on sale
        else:
            item_total = item.price * item_quantity  # Use regular price if not on sale
        
        cart_total += item_total  # Add to the cart total
    print(cart_total)

    return render(req, 'cart.html', {
        'cart_items': cart_items,
        'quantity_range': quantity_range,
        'quantity': quantity,  # Pass quantities to the template
        'cart_total': cart_total,  # Pass the cart total to the template
    })



  

def cart_update(req):
    cart = Cart(req)

    if req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        quantity = int(req.POST.get('quantity'))  # Capture the quantity from the POST data

        product = get_object_or_404(Product, id=product_id)
        
        cart.update(product=product, quantity=quantity)  # Add product with quantity

        cart_number = cart.__len__()  # Get the number of items in the cart

        # Return response as JSON
        response = JsonResponse({'Cart_number': cart_number})
        return response
    return render(req, 'cart.html')

    
    

def cart_delete(req, id):
    cart = Cart(req)
    cart.cart_delete(id)
    cart_items = cart.cart_get()  # Call cart_get() to fetch updated cart items
    return redirect('cart_get')

    

def cart_add(req):
    # Get the Cart instance
    cart = Cart(req)

    if req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        quantity = int(req.POST.get('quantity'))  # Capture the quantity from the POST data

        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=quantity)  # Add product with quantity

        cart_number = cart.__len__()  # Get the number of items in the cart

        # Return response as JSON
        response = JsonResponse({'Cart_number': cart_number})
        return response
    return render(req, 'cart.html')


