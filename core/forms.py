from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Used on the checkout page for applying coupons
class CouponForm(forms.Form):
    code = forms.CharField(max_length=20, label='Coupon Code')

# Registration form for new users
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Used in the cart view for applying coupons
class CouponApplyForm(forms.Form):
    code = forms.CharField(max_length=50)
