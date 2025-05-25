from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm,Payment_Form
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Profile
# Create your views here.

def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:

        return render(request, "payment/not_shipped_dash.html", {})
    else:

        messages.success(request,'Access denied')
        return redirect('home')
    

def not_shipped_dash(request):
    return render(request, "payment/shipped_dash.html", {})
    messages.success(request,'order placed')
    return redirect('home')
    


def process_order(request):
    if request.POST:
        cart=Cart(request)
        cart_products = cart.get_prods 
        quantities = cart.get_quants
        totals = cart.cart_total()

        #get billing info from the last page
        payment_form=Payment_Form(request.POST or None)
        #get shipping session data
        my_shipping = request.session.get('my_shipping')

        #gather order info
        full_name=my_shipping['shipping_fullname']
        email=my_shipping['shipping_email']
        #create shipping address from session
        shipping_address=f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_pincode']}\n{my_shipping['shipping_country']}\n"
        amount_paid=totals
        #create an order
        
        if request.user.is_authenticated:
            #logged in
            user =request.user
            #create order
            create_order = Order(user=user,full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
            create_order.save()

            #add order items
            #get the order id
            order_id=create_order.pk
            #get product info
            for product in cart_products():
                #get product id
                product_id =product.id
                #get product price
                if product.is_sale:
                    price=product.sale_price
                else:
                    price=product.price
                #get quantity
                for key,value in quantities().items():
                    if int(key) ==product.id:
                        #create order items
                        create_order_item=OrderItem(order_id=order_id,product_id=product_id,user_id=user.id,quantity=value,price=price)
                        create_order_item.save()
            #delete our cart after checkout
            for key in list(request.session.keys()):
                if key=='session_key':
                    #delete session key of cart
                    del request.session[key]


            )
            return redirect('messages.success(request, "order placed"home')
        else:
            #not logged in
            create_order = Order(user=user,full_name=full_name,email=email,shipping_address=shipping_address,amount_paid=amount_paid)
            create_order.save()
            # Add order items
			
			# Get the order ID
            order_id = create_order.pk
			
			# Get product Info
            for product in cart_products():
                        
				# Get product ID
                product_id = product.id
				# Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

				# Get quantity
                for key,value in quantities().items():
                    if int(key) == product.id:
						# Create order item
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
                        create_order_item.save()

			# Delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
					# Delete the key
                    del request.session[key]
            messages.error(request, "order placed")
            return redirect('home')
        

    else:
        messages.error(request, "Access Denied")
        return redirect('home')
        

def payment_success(request):
    return render(request,"payment/payment_success.html",{})


def checkout(request):

    #get cart
    cart=Cart(request)
    cart_products = cart.get_prods 
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request,"payment/checkout.html",{"cart_products":cart_products, 'quantities':quantities,"totals":totals,"shipping_form":shipping_form})

    else:
        #checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request,"payment/checkout.html",{"cart_products":cart_products, 'quantities':quantities,"totals":totals,"shipping_form":shipping_form})

def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        totals = cart.cart_total()
        
        #create a session with shipping info
        my_shipping =request.POST
        request.session['my_shipping']=my_shipping

        #check user logged in
        if request.user.is_authenticated:
            #get the billing form
            billing_form=Payment_Form

            return render(request, "payment/billing_info.html", {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_info":request.POST,
            'billing_form':billing_form,
        })
        
        else:
            return render(request, "payment/billing_info.html", {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_info":request.POST,
            'billing_form':billing_form,
        })
             
        #deleted form unwanted
    else:
        messages.error(request, "Access Denied")
        return redirect('home')











    '''  
        shipping_form = request.POST  # just pass raw data for now

        return render(request, "payment/billing_info.html", {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
        })'''
    