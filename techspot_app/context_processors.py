from .models import *
from django.shortcuts import *
from handler.getcartshandler import *


def get_common_context(request, products=None, extra_context=None):
    user, cart_items, total_items_count, grand_total = get_cart_context(request)

    context = {
        "categories": CategoryModel.objects.prefetch_related("subcategories").all(),
        "sub_categories": Sub_CategoryModel.objects.all(),
        "images": image_SliderModel.objects.all(),
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
        "header": HeaderModel.objects.last(),
        "otherdetails": OtherDetailModel.objects.last(),
        "advertisement": AdvertisementModel.objects.all(),
        "allcategory": CategoryModel.objects.all(),
    }

    if products:
        context["products"] = products
    if extra_context:
        context.update(extra_context)

    return context
