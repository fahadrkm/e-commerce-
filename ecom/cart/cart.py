# for session 
from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session

        self.request = request

        #get current session key
        cart = self.session.get('session_key')
        
        #if the user is new , no session key so create new
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

            #make sure cart is available on all pages of site
        self.cart =cart


        
    def add(self,product):
        product_id = str(product.id)
        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={'price': str(product.price)}

        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        #getids fromcart
        product_ids = self.cart.keys()
        #use id to look up product in db
        products= Product.objects.filter(id__in=product_ids)
        
        #return to those looked up products
        return products

    


