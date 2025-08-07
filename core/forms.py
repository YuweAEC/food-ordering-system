from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CouponForm(forms.Form):
    code = forms.CharField(max_length=20, label='Coupon Code')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


### views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, Coupon
from .forms import CouponForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
    order = get_object_or_404(Order, user=request.user, ordered=False)
    form = CouponForm()
    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'core/checkout.html', context)

@login_required
def apply_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code=code, active=True)
                order = Order.objects.get(user=request.user, ordered=False)
                order.coupon = coupon
                order.final_price = order.get_total_after_discount()
                order.save()
                messages.success(request, "Coupon applied successfully!")
            except Coupon.DoesNotExist:
                messages.error(request, "Invalid or expired coupon.")
    return redirect('checkout')