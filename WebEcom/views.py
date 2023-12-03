from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from datetime import datetime, timedelta  
from django.db import models
from .models import *
from django.utils import timezone
from django.db.models import Q
from django.core.serializers import serialize
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "index.html")
def info(request):
    return render(request, "page1.html")
def about(request):
    return render(request, "page2.html")
def productlist(request):
    proudct_list = Product.objects.all()
    proudct_list = proudct_list.filter(Is_active = True)
    return render(request, "productlist.html",{"list_product":proudct_list})
def Product_data(request,product_code):
    if request.method == "POST":
        print(request.POST)
        return HttpResponseRedirect("cartdetail")

        
    try:
        Product_ = Product.objects.get(Product_Code = product_code)
        print(Product_ )
  
        list_img = Product_Img.objects.filter(Product = Product_)
        return render(request, "Product_Detial.html",{"Product":Product_,"list_img":list_img})
    except:
            redirect("productlist")    

def cartdetail(request):
    return render(request, "Cartdetails.html")
def cartPayment(request):
    return render(request, "CartPayment.html")