from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('products', views.product_list, name='product_list'),
    path('product-detail/<int:pid>', views.product_detail, name='product_detail'),
    path('cart', views.wozti_cart, name='wozti_cart'),
    path('wishlist', views.wish_list, name='wish_list'),
    path('checkout', views.checkout, name='checkout'),
    path('myAccount', views.myAccount, name='myAccount'),
    path('contact', views.contact, name='contact'),
    path('addproduct', views.Add_Product_Form, name='addproduct'),
]