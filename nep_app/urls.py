from django.conf import settings
from django.conf.urls.static import *
from django.urls import path
from django.conf.urls import *
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("gym/", gym, name="gym"),
    path("shop/", shop, name="shop"),
    path("gaming/", gaming, name="gaming"),
    path("cart/", cart_detail, name="cart_Detail"),
    path("contactus/", contact_us, name="contactus"),
    path("tele_shopping_nepal/", tele_shopping_nepal, name="tele_shopping_nepal"),
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
    #
    #
    # search
    path("search/", search_query, name="search_query"),
    #
    #
    # dashboard
    path("dashboard/", dashboard, name="dashboard"),
    #
    # authentication
    path("accounts/login/", user_login, name="login"),
    path("accounts/register/", user_register, name="register"),
    path("logout/", user_logout, name="logout"),
    #
    #
    # pages
    path("new_user_guide/", new_user_guide, name="new_user_guide"),
    path("shipping_charges/", shipping_charges, name="shipping_charges"),
    path("delivery_timeline/", delivery_timeline, name="delivery_timeline"),
    path("order_tracking/", order_tracking, name="order_tracking"),
    path("faq/", faq, name="faq"),
    path("terms_and_condition/", terms_and_condition, name="terms_and_condition"),
    path("return_refund/", return_refund, name="return_refund"),
    path("checkout/", checkout, name="checkout"),
    path("canceling_order/", canceling_order, name="canceling_order"),
    path("return_product/", return_product, name="return_product"),
    path("my_orders/", my_orders, name="my_orders"),
    path("blog/", blog, name="blog"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
