from django.shortcuts import render,redirect
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.forms import SignUpForm, UpdateUserForm,ChangePasswordForm
from django import forms

def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')

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


    
