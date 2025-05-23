from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(
    [
        UserModel,
        image_SliderModel,
        CategoryModel,
        Sub_CategoryModel,
        ProductModel,
        CartItemModel,
        CartModel,
        ShippingInfoModel,
        OrderModel,  
        OrderItemModel,
        HeaderModel,
        OtherDetailModel,
        AdvertisementModel,
        SocialMediaModel,
    ]
)
