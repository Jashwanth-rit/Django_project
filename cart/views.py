from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_get(req):
    return render(req, 'cart.html', {  # Direct reference to 'home.html'
       
    })

def cart_update(req):
    return render(req, 'cart.html', {  # Direct reference to 'home.html'
       
    })

def cart_delete(req):
    return render(req, 'cart.html', {  # Direct reference to 'home.html'
       
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

