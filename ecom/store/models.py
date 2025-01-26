from django.db import models
import datetime

#cat of prdouct
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    #plralise category into categories

    class Meta:
        verbose_name_plural = 'categories'
        

    

class customer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=7)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=250,default='',null=True)
    image=models.ImageField(upload_to='uploads/product/')
    #add sales
    is_sale= models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    


    def __str__(self):
        return self.name


class order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=250,default='',blank=True)
    phone=models.CharField(max_length=10,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product


