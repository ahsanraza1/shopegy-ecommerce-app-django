# from curses.ascii import HT
import re
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, RegistrationForm, Add_Product
from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, Category

# Create your views here.

def Add_Product_Form(request):
    form = Add_Product()
    return render( request, 'store/addproduct.html', { 'form':form})

def check_auth(request):
    current_user = request.user
    if current_user.is_authenticated:
        return True
    return False

def index( request ):
    return render( request, 'store/index.html', { 'LoggedUser' : check_auth(request) })

def product_list( request ):
    p = prd = Product.get_all_products()
    for pr in p:
        pr.name = pr.name if len(pr.name) < 20 else pr.name[:15]+'...'
        
    c = Category.get_all_categories()
    context = {
        'categories'   : c,
        'products' : p,
        'LoggedUser' : check_auth(request)
    }
    return render( request, 'store/product-list.html', context )

def product_detail(request, pid):
    product = Product.objects.get(pk=pid)
    c = Category.get_all_categories()
    return render( request, 'store/product-detail.html', { 'LoggedUser' : check_auth(request), 'product': product, 'categories': c})

def wozti_cart( request ):
    return render( request, 'store/cart.html', { 'LoggedUser' : check_auth(request) })

def wish_list( request ):
    return render( request, 'store/wishlist.html', { 'LoggedUser' : check_auth(request) })


def checkout( request ):
    return render( request, 'store/checkout.html', { 'LoggedUser' : check_auth(request) })

def myAccount( request ):
    return render( request, 'store/my-account.html', { 'LoggedUser' : check_auth(request) })

def contact( request ):
    return render( request, 'store/contact.html', { 'LoggedUser' : check_auth(request) })


def register( request ):
    if request.method == 'POST':
        form = RegistrationForm( request.POST )
        if form.is_valid:
            try:
                form.save()
            except:
                return render( request, 'store/login.html', {'form': form, 'logged' : check_auth(request), 'LoggedUser' : check_auth(request)})
            return redirect( login_user )
            # return HttpResponse("<h4>Register successfull</h4>")
        else:
            return HttpResponse("<h4>Register Crashed</h4>")
    form = RegistrationForm()
    return render( request, 'store/login.html', {'form': form, 'logged' : check_auth(request), 'LoggedUser' : check_auth(request)})
# 

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # try:
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate( email = email, password=password)
                if user is not None:
                    login(request, user)
                    # messages.info(request, f"You are now logged in as {email}.")
                    return redirect( index )
                else:
                    return render( request, 'store/login.html', {'form': form, 'logged' : check_auth(request), 'err': True, 'LoggedUser' : check_auth(request)})
                    #messages.error(request,'Invalid username or password.')
            # except:
            #     return render( request, 'store/login.html', {'form': form, 'logged' : check_auth(request), 'err': True})            
        else:
            return HttpResponse("sdvbsm")
    form = LoginForm()
    return render(request=request, template_name="store/login.html", context={"form":form, 'logged' : check_auth(request), 'LoggedUser' : check_auth(request)})

# 
# 
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        try:
            return redirect(request.META['HTTP_REFERER'], LoggedUser = check_auth(request) )
        except:
            return redirect( index, LoggedUser = check_auth(request) )
    else:
        return HttpResponse( "Forbidden URL : No account has been logged in" )
    # try:
    #     prev_url = request.META['HTTP_REFERER']
    #     logout(request)
    #     # checkLog = check_auth(request)
    #     # if check_auth:
    #     #     LoggedUser =  request.user
    #     # else:
    #     #     LoggedUser = False
    #     return redirect(request.META['HTTP_REFERER'])
    # except:
    #     # return redirect( index , UserLogged = LoggedUser )
    # # else:
    #     return HttpResponse( "Forbidden URL" )
    

    
            # return render( request, 'store/index.html', { 'logged' : check_auth(request)})    
        # return redirect(f'{redirect_url}?{parameters}')
        # return render( request, request.META['HTTP_REFERER'], { 'logged' : check_auth(request)})
