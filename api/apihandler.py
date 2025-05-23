from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view


class SetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


def get_apihandler(request, model, model_serializer, title):
    try:
        datas = model.objects.all()
        paginator = SetPagination()
        result_page = paginator.paginate_queryset(datas, request)
        serializer = model_serializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response(
            {"message": f"Failed to retrive {title}", "error": str(e)},
            status=status.HTTP_400_BAD_REQUEST,
        )


def create_apihandler(request, model_serializer, title):
    try:
        serializer = model_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"message": "Validation failed", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as e:
        return Response(
            {"message": f"Failed to create {title} ", "error": str(e)},
            status=status.HTTP_400_BAD_REQUEST,
        )


def getbyid_apihandler(request, id, title, model, model_serializer):
    try:
        datas = get_object_or_404(model, id=id)
        serializer = model_serializer(datas)
        return Response(
            {"message": f"{title} Found :)", 
             "data": serializer.data
             },
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {"message": f"{title} not found", "error": str(e)},
            status=status.HTTP_404_NOT_FOUND,
        )


def update_apihandler(
    request,
    id,
    model,
    model_serializer,
    title,
):
    try:
        datas = model.objects.get(id=id)
    except model.DoesNotExist:
        return Response(
            {"message": f"{title} not found"}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = model_serializer(datas, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": f"{title} updated successfully", "data": serializer.data},
            status=status.HTTP_202_ACCEPTED,
        )

    return Response(
        {"message": f"{title} update failed", "errors": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )


def delete_apihandler(request, id, model, title):
    try:
        datas = get_object_or_404(model, id=id)
        datas.delete()
        return HttpResponse(
            {f"{title} Deleted Successfully"}, status.HTTP_204_NO_CONTENT
        )
    except:
        return HttpResponse({"Deletion Failed"}, status=status.HTTP_400_BAD_REQUEST)
