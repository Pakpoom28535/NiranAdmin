
from django.contrib import admin
from django.urls import path, include
from adminlte import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('login', views.signin, name='login'),
     path('sale', views.sale, name='sale'),
      path('product', views.product, name='product'),
       path('addproduct', views.addproduct, name='addproduct'),
        path('editproduct/<int:product_id>', views.editproduct, name='editproduct'),
          path('orderdeital/<int:order_id>', views.orderdetial, name='orderdetial'),
        path('signout', views.signout, name='signout'),
]