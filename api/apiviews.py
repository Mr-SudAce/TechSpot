from django.http import HttpResponse
from techspot_main.settings import base_url
from .apihandler import *
from .serializers import *

# Create your views here.


def index(request):
    return HttpResponse(f"Hello, world. You're at the polls index. {base_url}")


# auth
@api_view(["GET"])
def GetUserAPI(request):
    return get_apihandler(
        request=request,
        model=UserModel,
        model_serializer=UserModelSerializer,
        title="User",
    )
@api_view(["POST"])
def CreateUserAPI(request):
    return create_apihandler(
        request=request, model_serializer=UserModelSerializer, title="User"
    )
@api_view(["GET"])
def GetUserByIdAPI(request, id):
    return getbyid_apihandler(
        id=id,
        request=request,
        title="User",
        model=UserModel,
        model_serializer=UserModelSerializer,
    )
@api_view(["PUT"])
def UpdateUserAPI(request, id):
    return update_apihandler(
        id=id,
        request=request,
        model=UserModel,
        model_serializer=UserModelSerializer,
        title="User",
    )
@api_view(["DELETE"])
def DeleteUserAPI(request, id):
    return delete_apihandler(id=id, request=request, model=UserModel, title="User")


# Product
@api_view(["GET"])
def GetProductAPI(request):
    return get_apihandler(
        request=request,
        model=ProductModel,
        model_serializer=ProductSerializer,
        title="Product",
    )
@api_view(["POST"])
def CreateProductAPI(request):
    return create_apihandler(
        request=request, model_serializer=ProductSerializer, title="Product"
    )
@api_view(["GET"])
def GetProductByIdAPI(request, id):
    return getbyid_apihandler(
        id=id,
        request=request,
        title="Product",
        model=ProductModel,
        model_serializer=ProductSerializer,
    )
@api_view(["PUT"])
def UpdateProductAPI(request, id):
    return update_apihandler(
        id=id,
        request=request,
        model=ProductModel,
        model_serializer=ProductSerializer,
        title="Product",
    )
@api_view(["DELETE"])
def DeleteProductAPI(request, id):
    return delete_apihandler(
        id=id, request=request, model=ProductModel, title="Product"
    )

# HeaderModel
@api_view(["GET"])
def GetHeaderAPI(request):
    return get_apihandler(
        request=request,
        model=HeaderModel,
        model_serializer=HeaderSerializer,
        title="Header",
    )
@api_view(["POST"])
def CreateHeaderAPI(request):
    return create_apihandler(
        request=request, model_serializer=HeaderSerializer, title="Header"
    )
@api_view(["GET"])
def GetHeaderByIdAPI(request, id):
    return getbyid_apihandler(
        request=request,
        id=id,
        model=HeaderModel,
        model_serializer=HeaderSerializer,
        title="Header",
    )
@api_view(["PUT"])
def UpdateHeaderAPI(request, id):
    return update_apihandler(
        id=id,
        request=request,
        model=HeaderModel,
        model_serializer=HeaderSerializer,
        title="Header",
    )
@api_view(["DELETE"])
def DeleteHeaderAPI(request, id):
    return delete_apihandler(
        request=request, id=id, model=HeaderModel, title="Header"
    )



# Image_SliderModel
@api_view(["GET"])
def GetSliderAPI(request):
    return get_apihandler(
        request=request,
        model=image_SliderModel,
        model_serializer=ImageSliderSerializer,
        title="Slider",
    )
@api_view(["POST"])
def CreateSliderAPI(request):
    return create_apihandler(
        request=request, model_serializer=ImageSliderSerializer, title="Slider"
    )
@api_view(["GET"])
def GetSliderByIdAPI(request, id):
    return getbyid_apihandler(
        request=request,
        id=id,
        model=image_SliderModel,
        model_serializer=ImageSliderSerializer,
        title="Slider",
    )
@api_view(["PUT"])
def UpdateSliderAPI(request, id):
    return update_apihandler(
        id=id,
        request=request,
        model=image_SliderModel,
        model_serializer=ImageSliderSerializer,
        title="Slider",
    )
@api_view(["DELETE"])
def DeleteSliderAPI(request, id):
    return delete_apihandler(
        request=request, id=id, model=image_SliderModel, title="Slider"
    )


# Catgeory
@api_view(["GET"])
def GetCategoryAPI(request):
    return get_apihandler(request=request, model=CategoryModel, model_serializer=CategorySerializer, title="Category")
@api_view(["POST"])
def CreateCategoryAPI(request):
    return create_apihandler(request=request, model_serializer=CategorySerializer, title="Category")
@api_view(["GET"])
def GetCategoryByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=CategoryModel, model_serializer=CategorySerializer, title="Category"
    )
@api_view(["PUT"])
def UpdateCategoryAPI(request, id):
    return update_apihandler(id=id, request=request, model=CategoryModel, model_serializer=CategorySerializer, title="Category")
@api_view(["DELETE"])
def DeleteCategoryAPI(request, id):
    return delete_apihandler(request=request, id=id, model=CategoryModel, title="Category")


# Sub_Category
@api_view(["GET"])
def GetSubCategoryAPI(request):
    return get_apihandler(
        request, Sub_CategoryModel, model_serializer=SubCategorySerializer, title="SubCategory"
    )
@api_view(["POST"])
def CreateSubCategoryAPI(request):
    return create_apihandler(request, model_serializer=SubCategorySerializer, title="SubCategory")
@api_view(["GET"])
def GetSubCategoryByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=Sub_CategoryModel, model_serializer=SubCategorySerializer, title="SubCategory"
    )
@api_view(["PUT"])
def UpdateSubCategoryAPI(request, id):
    return update_apihandler(
        id=id, request=request, model=Sub_CategoryModel, model_serializer=SubCategorySerializer, title="SubCategory"
    )
@api_view(["DELETE"])
def DeleteSubCategoryAPI(request, id):
    return delete_apihandler(request=request, id=id, model=Sub_CategoryModel, title="SubCategory")


# cart model
@api_view(["GET"])
def GetCartAPI(request):
    return get_apihandler(request=request, model=CartModel, model_serializer=CartSerializer, title="Cart")
@api_view(["POST"])
def CreateCartAPI(request):
    return create_apihandler(request=request, model_serializer=CartSerializer, title="Cart")
@api_view(["GET"])
def GetCartByIdAPI(request, id):
    return getbyid_apihandler(request=request, id=id, model=CartModel, model_serializer=CartSerializer, title="Cart")
@api_view(["PUT"])
def UpdateCartAPI(request, id):
    return update_apihandler(id=id, request=request, model=CartModel, model_serializer=CartSerializer, title="Cart")
@api_view(["DELETE"])
def DeleteCartAPI(request, id):
    return delete_apihandler(request=request, id=id, model=CartModel, title="Cart")


# cartItem model
@api_view(["GET"])
def GetCartItemAPI(request):
    return get_apihandler(request, model=CartItemModel, model_serializer=CartItemSerializer, title="CartItem")
@api_view(["POST"])
def CreateCartItemAPI(request):
    return create_apihandler(request=request, model_serializer=CartItemSerializer, title="CartItem")
@api_view(["GET"])
def GetCartItemByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=CartItemModel, model_serializer=CartItemSerializer, title="CartItem"
    )
@api_view(["PUT"])
def UpdateCartItemAPI(request, id):
    return update_apihandler(id=id, request=request, model=CartItemModel, model_serializer=CartItemSerializer, title="CartItem")
@api_view(["DELETE"])
def DeleteCartItemAPI(request, id):
    return delete_apihandler(request=request, id=id, model=CartItemModel, title="CartItem")


# ShippingInfo Model
@api_view(["GET"])
def GetShippingInfoAPI(request):
    return get_apihandler(
        request=request, model=ShippingInfoModel, model_serializer=ShippingInfoSerializer, title="ShippingInfo"
    )
@api_view(["POST"])
def CreateShippingInfoAPI(request):
    return create_apihandler(request, model_serializer=ShippingInfoSerializer, title="ShippingInfo")
@api_view(["GET"])
def GetShippingInfoByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=ShippingInfoModel, model_serializer=ShippingInfoSerializer, title="ShippingInfo"
    )
@api_view(["PUT"])
def UpdateShippingInfoAPI(request, id):
    return update_apihandler(
        id=id, request=request, model=ShippingInfoModel, model_serializer=ShippingInfoSerializer, title="ShippingInfo"
    )
@api_view(["DELETE"])
def DeleteShippingInfoAPI(request, id):
    return delete_apihandler(request=request, id=id, model=ShippingInfoModel, title="ShippingInfo")


# order
@api_view(["GET"])
def GetOrderAPI(request):
    return get_apihandler(request=request, model=OrderModel, model_serializer=OrderSerializer, title="Order")
@api_view(["POST"])
def CreateOrderAPI(request):
    return create_apihandler(request=request, model_serializer=OrderSerializer, title="Order")
@api_view(["GET"])
def GetOrderByIdAPI(request, id):
    return getbyid_apihandler(request=request, id=id, model=OrderModel, model_serializer=OrderSerializer, title="Order")
@api_view(["PUT"])
def UpdateOrderAPI(request, id):
    return update_apihandler(id=id, request=request, model=OrderModel, model_serializer=OrderSerializer, title="Order")
@api_view(["DELETE"])
def DeleteOrderAPI(request, id):
    return delete_apihandler(request=request, id=id, model=OrderModel, title="Order")


# orderitem
@api_view(["GET"])
def GetOrderItemAPI(request):
    return get_apihandler(request=request, model=OrderItemModel, model_serializer=OrderItemSerializer, title="OrderItem")
@api_view(["POST"])
def CreateOrderItemAPI(request):
    return create_apihandler(request=request, model_serializer=OrderItemSerializer, title="OrderItem")
@api_view(["GET"])
def GetOrderItemByIdAPI(request, id):
    return getbyid_apihandler(request=request, id=id, model=OrderItemModel, model_serializer=OrderItemSerializer, title="OrderItem")
@api_view(["PUT"])
def UpdateOrderItemAPI(request, id):
    return update_apihandler(id=id, request=request, model=OrderItemModel, model_serializer=OrderItemSerializer, title="OrderItem")
@api_view(["DELETE"])
def DeleteOrderItemAPI(request, id):
    return delete_apihandler(request=request, id=id, model=OrderItemModel, title="OrderItem")


# orderdetail model
@api_view(["GET"])
def GetOtherDetailAPI(request):
    return get_apihandler(
        request=request, model=OtherDetailModel, model_serializer=OtherDetailSerializer, title="OtherDetail"
    )
@api_view(["POST"])
def CreateOtherDetailAPI(request):
    return create_apihandler(request=request, model_serializer=OtherDetailSerializer, title="OtherDetail")
@api_view(["GET"])
def GetOtherDetailByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=OtherDetailModel, model_serializer=OtherDetailSerializer, title="OtherDetail"
    )
@api_view(["PUT"])
def UpdateOtherDetailAPI(request, id):
    return update_apihandler(
        id=id, request=request, model=OtherDetailModel, model_serializer=OtherDetailSerializer, title="OtherDetail"
    )
@api_view(["DELETE"])
def DeleteOtherDetailAPI(request, id):
    return delete_apihandler(request=request, id=id, model=OtherDetailModel, title="OtherDetail")


# Advertisement
@api_view(["GET"])
def GetAdvertisementAPI(request):
    return get_apihandler(
        request=request, model=AdvertisementModel, model_serializer=AdvertisementSerializer, title="Advertisement"
    )
@api_view(["POST"])
def CreateAdvertisementAPI(request):
    return create_apihandler(request=request, model_serializer=AdvertisementSerializer, title="Advertisement")
@api_view(["GET"])
def GetAdvertisementByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=AdvertisementModel, model_serializer=AdvertisementSerializer, title="Advertisement"
    )
@api_view(["PUT"])
def UpdateAdvertisementAPI(request, id):
    return update_apihandler(
        id=id, request=request, model=AdvertisementModel, model_serializer=AdvertisementSerializer, title="Advertisement"
    )
@api_view(["DELETE"])
def DeleteAdvertisementAPI(request, id):
    return delete_apihandler(request=request, id=id, model=AdvertisementModel, title="Advertisement")


# socialmedia model
@api_view(["GET"])
def GetSocialMediaAPI(request):
    return get_apihandler(
        request=request, model=SocialMediaModel, model_serializer=SocialMediaSerializer, title="SocialMedia"
    )
@api_view(["POST"])
def CreateSocialMediaAPI(request):
    return create_apihandler(request=request, model_serializer=SocialMediaSerializer, title="SocialMedia")
@api_view(["GET"])
def GetSocialMediaByIdAPI(request, id):
    return getbyid_apihandler(
        request=request, id=id, model=SocialMediaModel, model_serializer=SocialMediaSerializer, title="SocialMedia"
    )
@api_view(["PUT"])
def UpdateSocialMediaAPI(request, id):
    return update_apihandler(
        id=id, request=request, model=SocialMediaModel, model_serializer=SocialMediaSerializer, title="SocialMedia"
    )
@api_view(["DELETE"])
def DeleteSocialMediaAPI(request, id):
    return delete_apihandler(request=request, id=id, model=SocialMediaModel, title="SocialMedia")
