
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterUserForm
from .models import Product

def home(req):
    products = Product.objects.all()
    return render(req, 'home.html', {  # Direct reference to 'home.html'
        "products": products,
    })
def product_details(req,id):
    product = Product.objects.get(pk = id)
    products = Product.objects.all()
    return render(req, 'product.html', {  # Direct reference to 'home.html'
        "product": product,
        "products": products,
    })



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
         messages.success(request,("there was an error in login, try again!"))
         return redirect('login')

    return render(request,'login.html',{})

def regist_user(request):
    if request.method == "POST":
       form = RegisterUserForm(request.POST)
       if form.is_valid():
          form.save()
          username = form.cleaned_data['username']
          password  =  form.cleaned_data['password1']
          user = authenticate(username = username,password = password)
          login(request,user)
          return redirect('home')
    else:
       form  = RegisterUserForm()
    return render(request,'register.html',{'form':form})



def logout_user(request):
    logout(request);
    

    return redirect('login')