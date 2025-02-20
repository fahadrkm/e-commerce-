from django.shortcuts import render,redirect
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.forms import SignUpForm 
from django import forms

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html',{'categories':categories})

def category(request, foo):
    foo = foo.replace('-', ' ')  # Replace hyphens with spaces
    try:
        category = Category.objects.get(name__iexact=foo)  # Case-insensitive lookup for category name
        products = Product.objects.filter(Category=category)  # Match the field name "Category"
        return render(request, 'category.html', {'products': products, 'category': category.name})
    except Category.DoesNotExist:
        messages.error(request, "That category doesn't exist.")
        return redirect('home')




def product(request,pk):
    product= Product.objects.get(id=pk)
    return render(request,'product.html', {'product':product})


def home(request):
    products = Product.objects.all()
    return render (request, 'home.html',{'products' : products})
 

def about(request):
    return render(request, 'about.html',{})

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("you have logged in successfull..."))
            return redirect('home')
        else:
            messages.success(request,("There is an error. Pleasse try again..."))
            return redirect('login')
    else:
        return render (request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out..."))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #login user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("you have Registered successfully..."))
            return redirect('home')
        else:
            messages.success(request,("there is a problem please try again..."))
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})


    
