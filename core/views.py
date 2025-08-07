from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import FoodItem, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required


def home(request):
    items = FoodItem.objects.all()
    return render(request, 'core/home.html', {'items': items})

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

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'core/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, item_id):
    item = FoodItem.objects.get(id=item_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, food_item=item)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')

@login_required
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items:
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            OrderItem.objects.create(order=order, food_item=item.food_item, quantity=item.quantity)
        cart_items.delete()
    return redirect('order_history')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'core/order_history.html', {'orders': orders})

@login_required
def profile(request):
    return render(request, 'core/profile.html')