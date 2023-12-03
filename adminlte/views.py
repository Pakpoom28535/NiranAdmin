from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from WebEcom.models import *
from django.http import JsonResponse
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
            return redirect('home')
        
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
    return render(request, "adminlte/dashborad.html")
def sale(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    return render(request, "adminlte/Sale.html")
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
        # try:
        #     Product_Img_ = Product_Img_()
        #     Product_Img_.Product = Product_
        #     Product_Img_.Product_Img = files['imgReport2']
        #     Product_Img_.save()
        # except:
        #     pass
        


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
        if fil1 != None and fil2 != None:
            for i in Product_img_:
                image_path = i.Product_Img.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                    i.delete()

            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil1
            new_pic.save()
            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil2
            new_pic.save()
        elif fil1 != None and fil2 == None:
  
            image_path = Product_img_.first().Product_Img.path
            if os.path.exists(image_path):
                os.remove(image_path)
                Product_img_.first().delete()
            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil1
            new_pic.save()
        elif fil1 == None and fil2 != None:
            if len(Product_img_) != 1:
                image_path = Product_img_.last().Product_Img.path
                if os.path.exists(image_path):
                    os.remove(image_path)
                    Product_img_.last().delete()
            
            new_pic = Product_Img()
            new_pic.Product = Product_
            new_pic.Product_Img = fil2
            new_pic.save()
        else:
            pass
   
    product_ = Product.objects.get(Product_id = product_id)
    product_img = Product_Img.objects.filter(Product= product_)
    return render(request, "adminlte/editproduct.html",{"product":product_,"img":product_img})