from django.contrib import admin
from.models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User

#reg model on main section thing
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#create an order item inline
class OrderItemInine(admin.StackedInline):
    model=OrderItem

#extend oyr order model
class OrderAdmin(admin.ModelAdmin):
    model=Order
    inlines=[OrderItemInine]
#unregister order model
admin.site.unregister(Order)

#reregister order and orderadmin
admin.site.register(Order,OrderAdmin)