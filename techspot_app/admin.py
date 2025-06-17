from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = UserChangeForm
    model = UserModel
    list_display = ('email', 'username', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'number')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'number', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(UserModel, CustomUserAdmin)

admin.site.register(
    [
        BlogModel, 
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
