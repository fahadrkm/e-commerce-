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
    extra=0

#extend oyr order model
class OrderAdmin(admin.ModelAdmin):
    model=Order
    readonly_fields=["date_ordered"]
    fields=["user","full_name","email","shipping_address","amount_paid","date_ordered","shipped"]
    inlines=[OrderItemInine]
#unregister order model
admin.site.unregister(Order)

#reregister order and orderadmin
admin.site.register(Order,OrderAdmin)