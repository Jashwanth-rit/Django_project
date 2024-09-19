from store.models import Product


class Cart:
    def __init__(self,req): 
        self.session = req.session

        # Get the current session key if it exists
        cart  = self.session.get('session_key')

        if 'session_key' not in req.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site

        self.cart = cart
    
    def add(self,product):
        product_id = str(product.id)

        #logic 
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def cart_get(self):
        # Get the product IDs from the cart
        product_ids = self.cart.keys()
        
        # Retrieve the products using the correct filter: id__in
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def cart_delete(self, product_id):
        # Ensure product_id is a string
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]  # Remove item from cart
            self.session.modified = True

