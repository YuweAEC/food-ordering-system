from rest_framework import serializers
from .models import FoodItem, CartItem, Order, Wishlist

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
