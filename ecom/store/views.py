from django.shortcuts import render,redirect
from . models import product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = product.objects.all()
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

    
