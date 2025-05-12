from django import forms
from .models import Order, Customer, Product
from django.contrib.auth.models import User


class StockUpdateForm(forms.Form):
    stock_quantity = forms.IntegerField(label="Stock Quantity")


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ordered_by", "shipping_address", "mobile", "email", "payment_method"]

    def clean_ordered_by(self):
        ordered_by = self.cleaned_data.get("ordered_by")

        if not ordered_by.replace(" ", "").isalpha():
            raise forms.ValidationError("Only characters are allowed.")
        return ordered_by


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(
        min_length=8, max_length=20, widget=forms.PasswordInput()
    )
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")

        if not uname.replace(" ", "").isalpha():
            raise forms.ValidationError("ERROR: Only Characters are allowed.")

        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("Customer with this username already exists.")
        return uname

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")

        if not full_name.replace(" ", "").isalpha():
            raise forms.ValidationError("ERROR: Only alphabetic characters are allowed.")
        return full_name

    def clean_address(self):
        address = self.cleaned_data.get("address")

        if not address.replace(" ", "").isalpha():
            raise forms.ValidationError("ERROR: Only characters are allowed.")
        return address

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email.lower().endswith("@gmail.com"):
            raise forms.ValidationError("Invalid email address")
        return email


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class ProductForm(forms.ModelForm):
    more_images = forms.FileField(
        required=False, widget=forms.FileInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "category",
            "image",
            "marked_price",
            "selling_price",
            "description",
            "warranty",
            "return_policy",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the product title here...",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the unique slug here...",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "marked_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Marked price of the product...",
                }
            ),
            "selling_price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Selling price of the product...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Description of the product...",
                    "rows": 5,
                }
            ),
            "warranty": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the product warranty here...",
                }
            ),
            "return_policy": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the product return policy here...",
                }
            ),
        }


class PasswordForgotForm(forms.Form):
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter the email used in customer account...",
            }
        )
    )

    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Customer.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError("Customer with this account does not exists..")
        return e


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
                "placeholder": "Enter New Password",
            }
        ),
        label="New Password",
    )
    confirm_new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "new-password",
                "placeholder": "Confirm New Password",
            }
        ),
        label="Confirm New Password",
    )

    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        confirm_new_password = self.cleaned_data.get("confirm_new_password")
        if new_password != confirm_new_password:
            raise forms.ValidationError("New Passwords did not match!")
        return confirm_new_password
