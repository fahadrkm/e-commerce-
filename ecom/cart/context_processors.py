# from .cart import Cart

# #create context processors so our cart work on all pages of the site

# def cart(request):
#     #return the default data from our cart
#     return {'cart':Cart(request)}

from .cart import Cart

# Create context processor so our cart can work on all pages of the site
def cart(request):
	# Return the default data from our Cart
	return {'cart': Cart(request)}