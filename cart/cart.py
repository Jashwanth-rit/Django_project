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
