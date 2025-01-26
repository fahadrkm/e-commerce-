from django.contrib import admin
from .models import category,customer,order,Product
# Register your models here.

admin.site.register(category)
admin.site.register(customer)
admin.site.register(Product)
admin.site.register(order)