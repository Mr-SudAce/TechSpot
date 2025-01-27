from django.conf import settings
from django.conf.urls.static import *
from django.urls import path
from django.conf.urls import *
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("cart/", cart_detail, name="cart_Detail"),
    #
    #
    # cart
    path("add-to-cart/<int:id>/", add_to_cart, name="add_to_cart"),
    path("cart/update_all/", update_all_cart_details, name="update_all_cart_details"),
    path("cartdetail/delete/<int:cart_det_id>/",cartdetail_delete,name="cartdetail_delete",),
    #
    #
    # productdetail
    path("product-detail/<int:id>/",product_itemView_detail, name="product_itemView_detail",),
    path("update-cart/<int:id>/", update_cart_quantity, name="update_cart_quantity"),
    #
    #
    # D_Content [add]
    path("dashboard/add-product/", add_product, name="add_product"),
    path("dashboard/add-category/", add_category, name="add_category"),
    path("dashboard/add-sub-category/", add_sub_category, name="add_sub_category"),
    path("dashboard/add-image-slider/", add_image_slider, name="add_image_slider"),
    path("dashboard/add-cart/", add_cart, name="add_cart"),
    path("dashboard/add-cart-item/", add_cart_item, name="add_cart_item"),
    path("dashboard/add_header_mid/", add_header_mid, name="add_header_mid"),
    path("dashboard/add_otherdetail/", add_otherdetail, name="add_otherdetail"),
    path("dashboard/add_advertisement/", add_advertisement, name="add_advertisement"),
    #
    #
    # D_Content [delete function]
    path("delete-product/<int:id>", del_product, name="del_product"),
    path("delete-category/<int:id>", del_category, name="del_category"),
    path("delete-sub-category/<int:id>", del_sub_category, name="del_sub_category"),
    path("delete-image-slider/<int:id>", del_image_slider, name="del_image_slider"),
    path("delete-cart/<int:id>", del_cart, name="del_cart"),
    path("delete-cart-item/<int:id>", del_cart_item, name="del_cart_item"),
    path("delete-header/<int:id>", del_header, name="del_header"),
    path("delete-otherdetail/<int:id>", del_otherdetail, name="del_otherdetail"),
    path("delete-advertisement/<int:id>", del_advertisement, name="del_advertisement"),
    #
    #
    # search
    path("search/", search_query, name="search_query"),
    #
    #
    # dashboard
    path("dashboard/", dashboard, name="dashboard"),
    #
    #
    # authentication
    path("accounts/login/", user_login, name="login"),
    path("accounts/register/", user_register, name="register"),
    path("logout/", user_logout, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
