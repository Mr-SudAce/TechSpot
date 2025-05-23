from rest_framework import serializers
from techspot_app.models import *

# --- User ---
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "username", "number", "email", "password", "is_active"]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = UserModel(**validated_data)
        (
            user.set_password(password)
            if hasattr(user, "set_password")
            else setattr(user, "password", password)
        )
        user.save()
        return user

# --- Product ---
class ProductSerializer(serializers.ModelSerializer):
    product_category_name = serializers.CharField(source='product_category.category_name', read_only=True)
    pro_sub_category_name = serializers.CharField(source='pro_sub_category.sub_category_name', read_only=True)

    discount_amount = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = [
            "id",
            "product_name",
            "product_description",
            "product_price",
            "product_image",
            "product_stock",
            "product_discount",
            "discount_amount",  # extra computed field
            "product_category",  # FK ID
            "product_category_name",  # readable name
            "pro_sub_category",
            "pro_sub_category_name",
        ]

    def get_discount_amount(self, obj):
        return obj.get_discount_amount()

# --- Header ---
class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderModel
        fields = '__all__'

# --- Image Slider ---
class ImageSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = image_SliderModel
        fields = '__all__'
        
# --- Category ---
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

# --- Sub Category ---
class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name', read_only=True)

    class Meta:
        model = Sub_CategoryModel
        fields = ['id', 'sub_category_icon', 'sub_category_name', 'category', 'category_name']

# --- Cart ---
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'

# --- Cart Item ---
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItemModel
        fields = ['id', 'cart', 'product', 'product_name', 'quantity', 'unit_price', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()

# --- Shipping Info ---
class ShippingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingInfoModel
        fields = '__all__'

# --- Order ---
class OrderSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = OrderModel
        fields = ['id', 'user', 'user_name', 'shipping_info', 'total_price', 'payment_method', 'status', 'created_at']

# --- Order Item ---
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)

    class Meta:
        model = OrderItemModel
        fields = ['id', 'order', 'product', 'product_name', 'quantity', 'price']

# --- Other Details ---
class OtherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherDetailModel
        fields = '__all__'

# --- Advertisement ---
class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementModel
        fields = '__all__'

# --- Social Media ---
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaModel
        fields = '__all__'

