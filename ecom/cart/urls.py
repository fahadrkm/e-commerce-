from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.cart_summary, name="cart_summary"),
   path('add/',views.cart_summary, name="cart_add"),
   path('delete/',views.cart_summary, name="cart_delete"),
   path('update/',views.cart_summary, name="cart_update"),
]
