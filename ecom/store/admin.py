from django.contrib import admin
from .models import category,customer,order,product
# Register your models here.

admin.site.register(category)
admin.site.register(customer)
admin.site.register(product)
admin.site.register(order)