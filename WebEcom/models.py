from django.db import models
import os
# Create your models here.
class Product(models.Model):
    Product_id =  models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=255)
    Product_Price = models.IntegerField()
    Product_Detial = models.CharField(max_length=255)
    Is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.Product_Code
class Product_Img(models.Model):
    Product_Img_id =  models.AutoField(primary_key=True)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    Product_Img =  models.ImageField(upload_to='reports/')  # 'reports/' is the directory where images will be stored
    def __str__(self):
        return self.Product.Product_Code
    def delete(self, *args, **kwargs):
        # Delete the associated image file before deleting the model instance
        if self.Product_Img:
            image_path = self.Product_Img.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)
class Token_Line(models.Model):
    Token_id =  models.AutoField(primary_key=True)
    Token_Code = models.CharField(max_length=255)
    def __str__(self):
        return self.Token_Code
class Shipping_Price(models.Model):
    Shipping_Pric_id =  models.AutoField(primary_key=True)
    Shipping_Price = models.IntegerField()
    def __str__(self):
        return self.Shipping_Price


class Orderhis(models.Model):
    Order_id = models.AutoField(primary_key=True)
    Order_code = models.CharField(max_length=255)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    t1 = models.CharField(max_length=255,null=True)
    t2 = models.CharField(max_length=255,null=True)
    log_img =  models.ImageField(upload_to='order/')  # 'reports/' is the directory where images will be stored
    color = models.CharField(max_length=255,null=True)
    t3 = models.TextField(null=True)
    t4 = models.CharField(max_length=255,null=True)
    t5 = models.TextField(null=True)
    t6 = models.CharField(max_length=255,null=True)
    t7 = models.CharField(max_length=255,null=True)
    qty = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    create_at = models.DateTimeField()
    status = models.BooleanField(null=True)
    status_change = models.DateTimeField(null=True)