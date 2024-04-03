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
import random
import string
# Create your views here.
def gencode():
    # Generate a random text of length 8
    random_text = ''.join(random.choices(string.ascii_letters, k=8))

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Combine the random text and number without a separator
    result = f"{random_text}{random_number}"

    return result
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
        data = request.POST
        files = request.FILES.get('img')
        print(files)
        Orderhis_ = Orderhis()
        Orderhis_.Order_code = gencode()
        Orderhis_.product = Product.objects.get(Product_Code = product_code)
        Orderhis_.t1 = data['t1']
        Orderhis_.t2 = data['t2']
        Orderhis_.t3 = data['t3']
        Orderhis_.t4 = data['t4']
        Orderhis_.t5 = data['t5']
        Orderhis_.t6 = data['t6']
        Orderhis_.t7 = data['t7']
        Orderhis_.color = data['color']
        Orderhis_.create_at = datetime.now()
        Orderhis_.log_img = files
        Orderhis_.save()
        return HttpResponseRedirect(f"cartdetail/{Orderhis_.Order_code}")
    try:
        Product_ = Product.objects.get(Product_Code = product_code)
        print(Product_ )
  
        list_img = Product_Img.objects.filter(Product = Product_)
        return render(request, "Product_Detial.html",{"Product":Product_,"list_img":list_img})
    except:
            redirect("productlist")    

def cartdetail(request,Order_code):
    data_ = Orderhis.objects.get(Order_code=Order_code)
    if request.method == "POST":
        print(request.POST)
        qty = int(request.POST.get('Qty', 0))
        if qty == 0:
            qty = 1
        data_.qty = qty
        total_ = qty * data_.product.Product_Price
        data_.total = total_
        data_.save()
        return HttpResponseRedirect(f"CartPayment/{data_.Order_code}",{"Orderhis":data_})
    print(Order_code)
    list_img = Product_Img.objects.filter(Product = data_.product).first()
    return render(request, "Cartdetails.html",{'Orderhis':data_,"list_img":list_img})
def cartPayment(request,Order_code):
    print(Order_code)
    data_ = Orderhis.objects.get(Order_code=Order_code)
    return render(request, "CartPayment.html",{'Orderhis':data_})