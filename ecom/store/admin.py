from django.contrib import admin
from .models import Category,customer,order,Product
# Register your models here.

admin.site.register(Category)
admin.site.register(customer)
admin.site.register(Product)
admin.site.register(order)