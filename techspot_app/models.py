from django.db import models
from django.conf import settings

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=600, unique=False, blank=False)
    number = models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.username} - {self.number} - {self.email}"


# Header////////////////////////////////
class HeaderModel(models.Model):
    header_image_left = models.ImageField(upload_to="header/", null=True, blank=True)
    header_image_right = models.ImageField(upload_to="header/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.header_image_left} - {self.header_image_right}"


class image_SliderModel(models.Model):
    image = models.ImageField(upload_to="slider/", default="")

    def __str__(self) -> str:
        return f"{self.image}"


class CategoryModel(models.Model):
    category_icon = models.CharField(max_length=200, default="", blank=True)
    category_name = models.CharField(max_length=200, default="", unique=True)
    category_image = models.ImageField(
        upload_to="category_image/", default="", blank=True
    )

    def __str__(self) -> str:
        return f"{self.category_name}"


class Sub_CategoryModel(models.Model):
    sub_category_icon = models.CharField(max_length=200, default="", blank=True)
    sub_category_name = models.CharField(max_length=200, default="", unique=True)
    category = models.ForeignKey(
        CategoryModel, related_name="subcategories", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.sub_category_name} - {self.category}"


class ProductModel(models.Model):
    product_category = models.ForeignKey(
        CategoryModel,
        related_name="productcategory",
        on_delete=models.CASCADE,
        default="",
    )
    product_name = models.CharField(max_length=200, default="")
    product_description = models.CharField(max_length=200, default="")
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    product_image = models.ImageField(
        upload_to="productImage/", default="", null=True, blank=True
    )
    pro_sub_category = models.ForeignKey(
        Sub_CategoryModel,
        related_name="productSubCategory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default="",
    )
    product_stock = models.IntegerField(default=0)
    product_discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def get_discount_amount(self):
        return self.product_price - (self.product_price * self.product_discount) / 100

    def __str__(self) -> str:
        return f"{self.product_name} - {self.product_description} - {self.product_price} - {self.product_category}"


# -----------------------------CARTS--------------------------------
class CartModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="cart")
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.user}"


class CartItemModel(models.Model):
    cart = models.ForeignKey(
        CartModel, on_delete=models.CASCADE, related_name="cart_items"
    )
    product = models.ForeignKey(
        ProductModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cart_items",
    )
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Snapshot of the price at the time the item was added",
    )

    def save(self, *args, **kwargs):
        if self.product and not self.unit_price:
            self.unit_price = self.product.product_price
        super().save(*args, **kwargs)

    def total_price(self):
        if self.unit_price is not None:
            return self.unit_price * self.quantity
        elif self.product and self.product.product_price is not None:
            return self.product.product_price * self.quantity
        return 0

    def __str__(self):
        product_name = self.product.product_name if self.product else "Deleted Product"
        return f"{product_name} x {self.quantity} in Cart #{self.cart.id}"


# Shopping////////////////////////////////
class ShippingInfoModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user} - {self.address}"


# Order////////////////////////////////
class OrderModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shipping_info = models.ForeignKey(ShippingInfoModel, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, default="COD")
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"


# OrderItem////////////////////////////////
class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.order} - {self.product}"


# otherDetail////////////////////////////////
class OtherDetailModel(models.Model):
    sm_link = models.CharField(max_length=200, default="", blank=True)
    email = models.CharField(max_length=200, default="", blank=True)
    phone_number = models.CharField(max_length=200, default="", blank=True)
    address = models.CharField(max_length=200, default="", blank=True)

    def __str__(self) -> str:
        return f"{self.sm_link} - {self.email} - {self.phone_number} - {self.address}"


class AdvertisementModel(models.Model):
    image = models.ImageField(upload_to="ad/", default="")

    def __str__(self) -> str:
        return f"{self.image}"


class SocialMediaModel(models.Model):
    icon = models.CharField(max_length=200, default="", blank=True)
    link = models.CharField(max_length=200, default="", blank=True)

    def __str__(self) -> str:
        return f"{self.icon} - {self.link}"
