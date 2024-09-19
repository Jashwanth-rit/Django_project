from store.models import Product

class Cart:
    def __init__(self, req): 
        self.session = req.session

        # Get the current session cart
        cart = self.session.get('session_key')

        if 'session_key' not in req.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    
    def add(self, product, quantity=1):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity  # Update quantity if already in cart
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity  # Add quantity to cart data
            }

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def cart_get(self):
        # Get the product IDs from the cart
        product_ids = self.cart.keys()

        # Retrieve the products from the database
        products = Product.objects.filter(id__in=product_ids)

        return products

    def cart_delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def get_quants(self):
        return {product_id: data['quantity'] for product_id, data in self.cart.items()}
