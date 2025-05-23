from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm,Payment_Form
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Profile
# Create your views here.

def process_order(request):
    if request.POST:
        pass

    else:
        pass

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
             

        shipping_form = request.POST  # just pass raw data for now

        return render(request, "payment/billing_info.html", {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
        })
    else:
        messages.error(request, "Access Denied")
        return redirect('home')
    
    