from django.contrib import admin
from django.contrib import admin
from .models import Category, FoodItem, CartItem, Order, OrderItem, User

admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
# admin.site.register(User)