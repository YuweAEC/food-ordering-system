from rest_framework import viewsets
from .models import FoodItem, CartItem, Wishlist
from .serializers import FoodItemSerializer, CartItemSerializer, WishlistSerializer

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
