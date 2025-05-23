from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from techspot_main.settings import base_url
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
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
        title="User"
    )
@api_view(["POST"])
def CreateUserAPI(request):
    return create_apihandler(
        request=request, model_serializer=UserModelSerializer, title="User"
    )
@api_view(["GET"])
def GetUserByIdAPI (request, id):
    return getbyid_apihandler(
        id=id,
        request=request,
        title="User",
        model= UserModel,
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
    return delete_apihandler(id=id, request=request, model=ProductModel, title="Product")


# 