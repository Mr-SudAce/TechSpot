from rest_framework import serializers
from techspot_app.models import *


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


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderModel
        fields = '__all__'
