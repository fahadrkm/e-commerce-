from django.contrib import admin
from.models import ShippingAddress,Order,OrderItem

#reg model on main section thing
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)