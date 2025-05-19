from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    address1=models.CharField(max_length=150)
    address2=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    pincode=models.CharField(max_length=150)
    country=models.CharField(max_length=150)

    #dont pluralise address
    class Meta:
        verbose_name_plural="shipping address"

    def __str__(self):
        return f'shipping address - {str(self.id)}'



