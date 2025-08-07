from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import FoodItem, CartItem, Order, OrderItem, Category, Wishlist
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Home with search and category filter
def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    items = FoodItem.objects.all()

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if category_id:
        items = items.filter(category_id=category_id)

    categories = Category.objects.all()
    wishlist = []
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user).values_list('item_id', flat=True)

    context = {
        'items': items,
        'categories': categories,
        'selected_category': category_id,
        'wishlist': wishlist
    }
    return render(request, 'core/home.html', context)


# Registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})


# View Cart
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'core/cart.html', {'cart_items': cart_items, 'total': total})


# Add to Cart
@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, food_item=item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')


# Place Order
@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items:
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, food_item=item.food_item, quantity=item.quantity)
        cart_items.delete()
    return redirect('order_history')


# Order History
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'core/order_history.html', {'orders': orders})


# Profile Page
@login_required
def profile(request):
    return render(request, 'core/profile.html')


#  Add to Wishlist
@login_required
def add_to_wishlist(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    Wishlist.objects.get_or_create(user=request.user, item=item)
    return redirect('home')


#  Remove from Wishlist
@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(FoodItem, id=item_id)
    Wishlist.objects.filter(user=request.user, item=item).delete()
    return redirect('home')
