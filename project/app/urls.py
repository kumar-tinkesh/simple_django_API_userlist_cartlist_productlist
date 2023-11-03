
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register', views.registration_view, name='registration_view'),
    path('index/', views.index, name='index'),
    path('user/', views.get_user, name='get_user'),

    path('login/', views.login_view, name='login_view'),
    path('product/', views.product_view, name='product_view'),
    path('plist/', views.get_product_list, name='get_product_list'),

    path('cart', views.add_to_cart, name='add_to_cart'),


]