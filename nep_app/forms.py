from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Add Product
class AddProductView(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_category', 'product_description', 'product_price', 'product_image', 'pro_sub_category', 'product_stock']

# Add Catgory
class AddCategoryView(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_icon', 'category_name', 'category_image']

# Add Cart Item
class AddCartItemView(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

# Add Cart
class AddCartView(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'is_paid']

# Add ImageSlider image
class AddImageSliderView(forms.ModelForm):
    class Meta:
        model = image_Slider
        fields = ['image']


# Add Sub_Category
class AddSub_CategoryView(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = ['sub_category_icon', 'sub_category_name', 'category']
        


class HeaderView(forms.ModelForm):
    class Meta:
        model = Header
        fields = ['header_image_left', 'header_image_right']


class OtherdetailsView(forms.ModelForm):
    class Meta:
        model = OtherDetail
        fields = ['sm_link', 'email', 'phone_number', 'address']
        