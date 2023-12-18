"""Niran URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from WebEcom import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('about', views.about, name='about'),
    path('Product/cartdetail/<str:Order_code>', views.cartdetail, name='cartdetail'),
    path('Product/cartdetail/CartPayment/<str:Order_code>', views.cartPayment, name='cartpayment'),
    #  path('cartpayment/<str:order_code>', views.cartPayment, name='cartpayment'),
    path('productlist', views.productlist, name='productlist'),
    path('Product/<str:product_code>', views.Product_data, name='Product'),

     
]
