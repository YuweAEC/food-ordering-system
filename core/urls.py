from django.urls import path
from . import views
from rest_framework import routers
from .api_views import FoodItemViewSet, CartItemViewSet, WishlistViewSet
from .views import CustomLoginView

# DRF Router for API endpoints
router = routers.DefaultRouter()
router.register(r'api/fooditems', FoodItemViewSet)
router.register(r'api/cartitems', CartItemViewSet)
router.register(r'api/wishlist', WishlistViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
    path('profile/', views.profile, name='profile'),
    path('wishlist/', views.Wishlist, name='wishlist'),
    path('wishlist/add/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    # Newly added
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

# Add API URLs from router
urlpatterns += router.urls
