from django.contrib import admin
from .apiviews import *
from django.urls import path

urlpatterns = [
    path("home/", index, name="apihome"),
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
]
