from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from WebEcom.models import *
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from datetime import datetime
# Create your views here.
# Create your views here.
def signout(request):
    print(request)
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
def signin(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            print(fname)
            return redirect('sale')
        
        else:
            messages.error(request, "Username หรือ Password ไม่ถูกต้อง")
            return redirect('signin')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, "adminlte/login.html")
def home(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method =="POST":
        print(request.POST)
        Orderhis_ = Orderhis.objects.get(Order_id = request.POST['order_id'])
        if request.POST['status'] == 'true':
            Orderhis_.status =True
        else: 
             Orderhis_.status =False
        Orderhis_.status_change = datetime.now()
        Orderhis_.save()
        return JsonResponse({"status":"ok"})
    data_ = Orderhis.objects.all()
    return render(request, "adminlte/Sale.html",{"list_data":data_})
def sale(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method =="POST":
        print(request.POST)
        Orderhis_ = Orderhis.objects.get(Order_id = request.POST['order_id'])
        if request.POST['status'] == 'true':
            Orderhis_.status =True
        else: 
             Orderhis_.status =False
        Orderhis_.status_change = datetime.now()
        Orderhis_.save()
        return JsonResponse({"status":"ok"})
    data_ = Orderhis.objects.all()
    return render(request, "adminlte/Sale.html",{"list_data":data_})
def orderdetial(request,order_id):
    Orderhis_ = Orderhis.objects.get(Order_id= order_id)
    print(Orderhis_.log_img)
    return render(request, "adminlte/orderdetial.html",{"Orderhis":Orderhis_})
def product(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method == "POST":
        print(request.POST)
        try:
            Product_ = Product.objects.get(Product_id=request.POST['remove_id'])
            Product_img_ = Product_Img.objects.filter(Product = Product_)
            for i in Product_img_:
                image_path = i.Product_Img.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            Product_.delete()
            return JsonResponse({"data":"ok"},status=200) 
        except Exception as e:
            return JsonResponse({"data":"ng","msg":"remove_error"},status=200) 
        
    proudct_list = Product.objects.all()
    proudct_list = proudct_list.filter(Is_active = True)
    return render(request, "adminlte/product.html",{"list_product":proudct_list})
def addproduct(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        files = request.FILES 
        Product_ = Product()
        Product_.Product_Code = data['Product_Code']
        Product_.Product_Detial = data['Product_Detial']
        Product_.Product_Price = data['Product_Price']
        Product_.save()
        Product_Img_ = Product_Img()
        Product_Img_.Product = Product_
        Product_Img_.Product_Img = files['imgReport']
        Product_Img_.save()
        try:
            Product_Img_ = Product_Img_()
            Product_Img_.Product = Product_
            Product_Img_.Product_Img = files['imgReport2']
            Product_Img_.save()
        except:
            pass
        


        print(files)
        return redirect('product')
    return render(request, "adminlte/addproduct.html")
def editproduct(request,product_id):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        if data['action'] == "remove":

            try:
                img_id = data['img_id']
                product_img_ = Product_Img.objects.get(Product_Img_id = img_id)
                product_img_.delete()

                return JsonResponse({"status":"ok"})
            except:
                return JsonResponse({"status":"ng"})
        files = request.FILES 
        print(files)
        Product_ = Product.objects.get(Product_id = product_id)
        Product_.Product_Code = data['Product_Code']
        Product_.Product_Detial = data['Product_Detial']
        Product_.Product_Price = data['Product_Price']
        if data['customCheck'] == 'on':
             Product_.Is_active = True
        else:
            Product_.Is_active = False
        Product_.save()
        fil1 = None
        fil2 = None
        Product_img_ = Product_Img.objects.filter(Product = Product_)
        try:
            fil1 = files['imgReport']
            
        except:
            pass
        try:
            fil2 = files['imgReport2']
        except:
            pass
        print(fil1)
        print(fil2)
        if fil1 != None :
            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil1
            new_pic.save()
           
        if fil2 != None:
            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil2
            new_pic.save()
        product_ = Product.objects.get(Product_id = product_id)
        product_img = Product_Img.objects.filter(Product= product_)
        return HttpResponseRedirect(f"{product_id}",{"product":product_,"img":product_img})
    product_ = Product.objects.get(Product_id = product_id)
    product_img = Product_Img.objects.filter(Product= product_).order_by("-Product_Img_id")
    return render(request, "adminlte/editproduct.html",{"product":product_,"img":product_img})