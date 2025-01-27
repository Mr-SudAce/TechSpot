from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# Add Product
class AddProductView(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


# Add Catgory
class AddCategoryView(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


# Add Cart Item
class AddCartItemView(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = "__all__"


# Add Cart
class AddCartView(forms.ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"


# Add ImageSlider image
class AddImageSliderView(forms.ModelForm):
    class Meta:
        model = image_Slider
        fields = "__all__"


# Add Sub_Category
class AddSub_CategoryView(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = "__all__"


class HeaderView(forms.ModelForm):
    class Meta:
        model = Header
        fields = "__all__"


class OtherdetailsView(forms.ModelForm):
    class Meta:
        model = OtherDetail
        fields = "__all__"


class AddAdvertisementView(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = "__all__"
