from django.contrib import admin
from .apiviews import *
from django.urls import path

urlpatterns = [
    path("", index, name="apihome"),
    
    # User
    path("user/", GetUserAPI, name="getuserapi"),
    path("user/create/", CreateUserAPI, name="createuserapi"),
    path("user/<int:id>/", GetUserByIdAPI, name="getuserbyidapi"),
    path("user/update/<int:id>/", UpdateUserAPI, name="updateuserapi"),
    path("user/delete/<int:id>/", DeleteUserAPI, name="deleteuserapi"),
    
    # Product
    path("product/", GetProductAPI, name="getproductapi"),
    path("product/create/", CreateProductAPI, name="createproductapi"),
    path("product/<int:id>/", GetProductByIdAPI, name="getproductbyidapi"),
    path("product/update/<int:id>/", UpdateProductAPI, name="updateproductapi"),
    path("product/delete/<int:id>/", DeleteProductAPI, name="deleteproductapi"),

    # Header
    path("header/", GetHeaderAPI, name="getheaderapi"),
    path("header/create/", CreateHeaderAPI, name="createheaderapi"),
    path("header/<int:id>/", GetHeaderByIdAPI, name="getheaderbyidapi"),
    path("header/update/<int:id>/", UpdateHeaderAPI, name="updateheaderapi"),
    path("header/delete/<int:id>/", DeleteHeaderAPI, name="deleteheaderapi"),

    # Slider
    path("slider/", GetSliderAPI, name="getsliderapi"),
    path("slider/create/", CreateSliderAPI, name="createsliderapi"),
    path("slider/<int:id>/", GetSliderByIdAPI, name="getsliderbyidapi"),
    path("slider/update/<int:id>/", UpdateSliderAPI, name="updatesliderapi"),
    path("slider/delete/<int:id>/", DeleteSliderAPI, name="deletesliderapi"),

    # Category
    path("category/", GetCategoryAPI, name="getcategoryapi"),
    path("category/create/", CreateCategoryAPI, name="createcategoryapi"),
    path("category/<int:id>/", GetCategoryByIdAPI, name="getcategorybyidapi"),
    path("category/update/<int:id>/", UpdateCategoryAPI, name="updatecategoryapi"),
    path("category/delete/<int:id>/", DeleteCategoryAPI, name="deletecategoryapi"),

    # SubCategory
    path("subcategory/", GetSubCategoryAPI, name="getsubcategoryapi"),
    path("subcategory/create/", CreateSubCategoryAPI, name="createsubcategoryapi"),
    path("subcategory/<int:id>/", GetSubCategoryByIdAPI, name="getsubcategorybyidapi"),
    path("subcategory/update/<int:id>/", UpdateSubCategoryAPI, name="updatesubcategoryapi"),
    path("subcategory/delete/<int:id>/", DeleteSubCategoryAPI, name="deletesubcategoryapi"),

    # Cart
    path("cart/", GetCartAPI, name="getcartapi"),
    path("cart/create/", CreateCartAPI, name="createcartapi"),
    path("cart/<int:id>/", GetCartByIdAPI, name="getcartbyidapi"),
    path("cart/update/<int:id>/", UpdateCartAPI, name="updatecartapi"),
    path("cart/delete/<int:id>/", DeleteCartAPI, name="deletecartapi"),

    # CartItem
    path("cartitem/", GetCartItemAPI, name="getcartitemapi"),
    path("cartitem/create/", CreateCartItemAPI, name="createcartitemapi"),
    path("cartitem/<int:id>/", GetCartItemByIdAPI, name="getcartitembyidapi"),
    path("cartitem/update/<int:id>/", UpdateCartItemAPI, name="updatecartitemapi"),
    path("cartitem/delete/<int:id>/", DeleteCartItemAPI, name="deletecartitemapi"),

    # ShippingInfo
    path("shippinginfo/", GetShippingInfoAPI, name="getshippinginfoapi"),
    path("shippinginfo/create/", CreateShippingInfoAPI, name="createshippinginfoapi"),
    path("shippinginfo/<int:id>/", GetShippingInfoByIdAPI, name="getshippinginfobyidapi"),
    path("shippinginfo/update/<int:id>/", UpdateShippingInfoAPI, name="updateshippinginfoapi"),
    path("shippinginfo/delete/<int:id>/", DeleteShippingInfoAPI, name="deleteshippinginfoapi"),

    # Order
    path("order/", GetOrderAPI, name="getorderapi"),
    path("order/create/", CreateOrderAPI, name="createorderapi"),
    path("order/<int:id>/", GetOrderByIdAPI, name="getorderbyidapi"),
    path("order/update/<int:id>/", UpdateOrderAPI, name="updateorderapi"),
    path("order/delete/<int:id>/", DeleteOrderAPI, name="deleteorderapi"),

    # OrderItem
    path("orderitem/", GetOrderItemAPI, name="getorderitemapi"),
    path("orderitem/create/", CreateOrderItemAPI, name="createorderitemapi"),
    path("orderitem/<int:id>/", GetOrderItemByIdAPI, name="getorderitembyidapi"),
    path("orderitem/update/<int:id>/", UpdateOrderItemAPI, name="updateorderitemapi"),
    path("orderitem/delete/<int:id>/", DeleteOrderItemAPI, name="deleteorderitemapi"),

    # OtherDetail
    path("otherdetail/", GetOtherDetailAPI, name="getotherdetailapi"),
    path("otherdetail/create/", CreateOtherDetailAPI, name="createotherdetailapi"),
    path("otherdetail/<int:id>/", GetOtherDetailByIdAPI, name="getotherdetailbyidapi"),
    path("otherdetail/update/<int:id>/", UpdateOtherDetailAPI, name="updateotherdetailapi"),
    path("otherdetail/delete/<int:id>/", DeleteOtherDetailAPI, name="deleteotherdetailapi"),

    # Advertisement
    path("advertisement/", GetAdvertisementAPI, name="getadvertisementapi"),
    path("advertisement/create/", CreateAdvertisementAPI, name="createadvertisementapi"),
    path("advertisement/<int:id>/", GetAdvertisementByIdAPI, name="getadvertisementbyidapi"),
    path("advertisement/update/<int:id>/", UpdateAdvertisementAPI, name="updateadvertisementapi"),
    path("advertisement/delete/<int:id>/", DeleteAdvertisementAPI, name="deleteadvertisementapi"),

    # SocialMedia
    path("socialmedia/", GetSocialMediaAPI, name="getsocialmediaapi"),
    path("socialmedia/create/", CreateSocialMediaAPI, name="createsocialmediaapi"),
    path("socialmedia/<int:id>/", GetSocialMediaByIdAPI, name="getsocialmediabyidapi"),
    path("socialmedia/update/<int:id>/", UpdateSocialMediaAPI, name="updatesocialmediaapi"),
    path("socialmedia/delete/<int:id>/", DeleteSocialMediaAPI, name="deletesocialmediaapi"),

]
