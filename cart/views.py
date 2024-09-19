from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_get(req):
    cart = Cart(req)
    cart_items = cart.cart_get()  # Call the method
    quantity = cart.get_quants()  # Get product quantities
    quantity_range = range(1, 11)  
    print("quantity",quantity)# Quantity selection range (1 to 10)

    return render(req, 'cart.html', {
        'cart_items': cart_items,
        'quantity_range': quantity_range,
        'quantity': quantity,  # Pass quantities to the template
    })

  

def cart_update(req):
    return render(req, 'cart.html', {  # Direct reference to 'home.html'
       
    })

def cart_delete(req, id):
    cart = Cart(req)
    cart.cart_delete(id)
    cart_items = cart.cart_get()  # Call cart_get() to fetch updated cart items

    return render(req, 'cart.html', {  # Use correct template name 'cart.html'
        'cart_items': cart_items
    })

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


