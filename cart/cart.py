class Cart:
    def __init__(self,req): 
        self.session = req.session

        # Get the current session key if it exists
        cart  = self.session.get('session_key')

        if 'session_key' not in req.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site

        self.cart = cart