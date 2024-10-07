
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .forms import RegisterUserForm, UpdateUserForm
from .models import Product
from django import template

from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UpdatePasswordForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UserProfileForm

@login_required
def user_info(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_info')  # Redirect to a success page

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'user_info.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UpdatePasswordForm(request.user)
    
    return render(request, 'updatepassword.html', {
        'form': form
    })




def home(request):
    query = request.GET.get('q')  # Get the search query
    if query:
        products = Product.objects.filter(name__icontains=query)  # Filter products by name
    else:
        products = Product.objects.all()  # Show all products when no search query

    return render(request, 'home.html', {  
        "products": products,
        "search_query": query  # Pass the search query to the template
    })

def product_details(req,id):
    product = Product.objects.get(pk = id)
    products = Product.objects.all()
    quantity_range = range(1, 11)
    return render(req, 'product.html', {  # Direct reference to 'home.html'
        "product": product,
        "products": products,
        'quantity_range': quantity_range
    })



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        
            return redirect('user_info')
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
          return redirect('user_info')
    else:
       form  = RegisterUserForm()
    return render(request,'register.html',{'form':form})

def user_profile(request):
    
    if request.user.is_authenticated:
       user = User.objects.get(id = request.user.id)
       form = UpdateUserForm(request.POST or None, instance = user)
       if form.is_valid():
          form.save()
          
          login(request,user)
          return redirect('home')
       return render(request,'user_profile.html',{'user_form':form})
    else:
       return render(request,'login.html',{})
       
# def user_info(request):
    
#     if request.user.is_authenticated:
#        user = User.objects.get(id = request.user.id)
#        form = UpdateUserForm(request.POST or None, instance = user)
#        if form.is_valid():
#           form.save()
          
#           login(request,user)
#           return redirect('home')
#        return render(request,'user_info.html',{'user_form':form})
#     else:
#        return render(request,'login.html',{})
    
    

def logout_user(request):
    logout(request);
    

    return redirect('login')