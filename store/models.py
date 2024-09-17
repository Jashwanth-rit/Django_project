from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField('first name',max_length= 100)
    last_name = models.CharField('last name',max_length= 100)
    phone = models.CharField('phone',max_length= 100)
    email = models.EmailField('email',max_length= 100)
    password = models.CharField('password',max_length= 100)
   

    def __str__(self):
        return self.first_name + " " + self.last_name


class Category(models.Model):
    name = models.CharField(' name',max_length= 100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'

       
    


class Product(models.Model):
    name = models.CharField('name',max_length= 100)
    price = models.DecimalField('price',decimal_places= 2,default=0,max_digits=100)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField('description',max_length= 250,default='',blank=True,null=True)
    image = models.ImageField('image',upload_to='uploads/product/')
    is_sale = models.BooleanField("sale",default=False)
    sale_price = models.DecimalField('sale price',decimal_places= 2,default=0,max_digits=100)

    def __str__(self):
        return self.name
    
class Order(models.Model):
   
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=20,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    

    def __str__(self):
        return self.product
