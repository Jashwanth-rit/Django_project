from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_get(req):

    cart = Cart(req)  # Pass the request to the Cart class
    cart_items = cart.cart_get  # Retrieve all items from the cart
    return render(req, 'cart.html', {'cart_items': cart_items})
  

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
# Get the Cart
    cart  = Cart(req)

    # Post

    if req.POST.get('action') == 'post':
        product_id = int(req.POST.get('product_id'))
        product  = get_object_or_404(Product,id = product_id)
        cart.add(product  = product)

        cart_number = cart.__len__()

        # response = JsonResponse({'product Name:':product.name})
        response = JsonResponse({'Cart_number':cart_number})
        return response
    return render(req, 'cart.html', {  # Direct reference to 'home.html'
       
    })

