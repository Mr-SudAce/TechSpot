from .models import *

def global_context(request):
    categories = CategoryModel.objects.prefetch_related("subcategories").all()
    sub_categories = Sub_CategoryModel.objects.all()
    sliders = image_SliderModel.objects.all()
    header = HeaderModel.objects.last()
    otherdetails = OtherDetailModel.objects.last()
    advertisement = AdvertisementModel.objects.all()
    allcategory = CategoryModel.objects.all()

    user_id = request.session.get("user_id")
    cart_items = []
    total_items_count = 0
    grand_total = 0.0

    if user_id:
        try:
            custom_user = UserModel.objects.get(id=user_id)
            if custom_user.is_active:
                cart = CartModel.objects.filter(user=custom_user.id, is_paid=False).first()
                if cart:
                    cart_items = CartItemModel.objects.filter(cart=cart)
        except UserModel.DoesNotExist:
            request.session.flush()

    # Filter out any cart items with missing products
    cart_items = [item for item in cart_items if item.product]
    total_items_count = len(cart_items)
    grand_total = sum(float(item.total_price()) for item in cart_items)

    return {
        "categories": categories,
        "sub_categories": sub_categories,
        "images": sliders,
        "header": header,
        "otherdetails": otherdetails,
        "advertisement": advertisement,
        "allcategory": allcategory,
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
    }
