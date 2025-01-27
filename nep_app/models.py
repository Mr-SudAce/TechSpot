from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_icon = models.CharField(max_length=200, default="", blank=True)
    category_name = models.CharField(max_length=200, default="", unique=True)
    category_image = models.ImageField(
        upload_to="category_image/", default="", blank=True
    )

    def __str__(self) -> str:
        return f"{self.category_name}"


class Sub_Category(models.Model):
    sub_category_icon = models.CharField(max_length=200, default="", blank=True)
    sub_category_name = models.CharField(max_length=200, default="", unique=True)
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.sub_category_name} - {self.category}"


class image_Slider(models.Model):
    image = models.ImageField(upload_to="slider/", default="")

    def __str__(self) -> str:
        return f"{self.image}"


class Product(models.Model):
    product_category = models.ForeignKey(
        Category, related_name="productcategory", on_delete=models.CASCADE, default=""
    )
    product_name = models.CharField(max_length=200, default="")
    product_description = models.CharField(max_length=200, default="")
    product_price = models.CharField(max_length=200, default="")
    product_image = models.ImageField(upload_to="productImage/", default="", null=True, blank=True)
    pro_sub_category = models.ForeignKey(
        Sub_Category,
        related_name="productSubCategory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    product_stock = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.product_name} - {self.product_description} - {self.product_price} - {self.product_category}"


# -----------------------------CARTS--------------------------------
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    is_paid = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.user}"


class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True
    )
    quantity = models.PositiveIntegerField(default=1,)

    def total_price(self):
        return float(self.product.product_price) * self.quantity

    def __str__(self) -> str:
        return f"{self.cart} - {self.quantity}"




# Header////////////////////////////////
class Header(models.Model):
    header_image_left = models.ImageField(upload_to="header/", null=True, blank=True)
    header_image_right = models.ImageField(upload_to="header/", null=True, blank=True)
    def __str__(self) -> str:
        return f"{self.header_image_left} - {self.header_image_right}"


# other detail////////////////////////////////
class OtherDetail(models.Model):
    sm_link = models.CharField(max_length=200, default="", blank=True)
    email = models.CharField(max_length=200, default="", blank=True)
    phone_number = models.CharField(max_length=200, default="", blank=True)
    address = models.CharField(max_length=200, default="", blank=True)
    def __str__(self) -> str:
        return f"{self.sm_link} - {self.email} - {self.phone_number} - {self.address}"
