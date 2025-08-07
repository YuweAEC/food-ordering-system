from django.contrib import admin
from .models import (Category,FoodItem,CartItem,Order,OrderItem,Coupon,Cart,)

# Registering existing models
admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)

# Registering new models
admin.site.register(Coupon)
admin.site.register(Cart)
