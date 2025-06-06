from django import forms
from .models import *
from django.core.validators import RegexValidator


from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserModel


class UserForm(forms.ModelForm):
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter your number",
                "oninput": 'this.value = this.value.replace(/[^0-9]/g, "")',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )

    class Meta:
        model = UserModel
        fields = ["username", "number", "email", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter your username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Secure password hashing
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text=(
            "Raw passwords are not stored, so there is no way to see this user's password, "
            'but you can change it using <a href="../password/">this form</a>.'
        )
    )

    class Meta:
        model = UserModel
        fields = [
            "email",
            "username",
            "number",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
        ]


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password"})
    )


# Add Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = "__all__"


# Add Catgory
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = "__all__"


# Add Cart Item
class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItemModel
        fields = "__all__"


# Add Cart
class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = "__all__"


# Add ImageSlider image
class ImageSliderForm(forms.ModelForm):
    class Meta:
        model = image_SliderModel
        fields = "__all__"


# Add Sub_Category
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_CategoryModel
        fields = "__all__"


class HeaderForm(forms.ModelForm):
    class Meta:
        model = HeaderModel
        fields = "__all__"


class OtherDetailForm(forms.ModelForm):
    class Meta:
        model = OtherDetailModel
        fields = "__all__"


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = AdvertisementModel
        fields = "__all__"


class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingInfoModel
        fields = ["address", "city", "postal_code", "phone_number"]
        widgets = {
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your address"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter your city"}
            ),
            "postal_code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter postal code"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter phone number"}
            ),
        }
