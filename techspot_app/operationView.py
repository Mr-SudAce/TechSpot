
from .models import *
from .forms import *
from handler.operationhandler import *




# Dashboard > D_Content
#
#
# Add/Create
def add_product(request):
    return handle_create(
        request=request,
        model=ProductModel,
        formname=ProductForm,
        redirect_url="add_product",
        template_url="Dashboard/D_Content/add_product.html",
        action_url="add_product",
    )


def add_category(request):
    return handle_create(
        request=request,
        model=CategoryModel,
        formname=CategoryForm,
        redirect_url="add_category",
        template_url="Dashboard/D_Content/add_category.html",
        action_url="add_category",
    )


def add_sub_category(request):
    return handle_create(
        request=request,
        model=Sub_CategoryModel,
        formname=SubCategoryForm,
        redirect_url="add_sub_category",
        template_url="Dashboard/D_Content/add_sub_category.html",
        action_url="add_sub_category",
    )


def add_image_slider(request):
    return handle_create(
        request=request,
        model=image_SliderModel,
        formname=ImageSliderForm,
        redirect_url="add_image_slider",
        template_url="Dashboard/D_Content/add_image_slider.html",
        action_url="add_image_slider",
    )


def add_cart(request):
    return handle_create(
        request=request,
        model=CartModel,
        formname=CartForm,
        redirect_url="add_cart",
        template_url="Dashboard/D_Content/add_cart.html",
        action_url="add_cart",
    )


def add_cart_item(request):
    return handle_create(
        request=request,
        model=CartItemModel,
        formname=CartItemForm,
        redirect_url="add_cart_item",
        template_url="Dashboard/D_Content/add_cart_item.html",
        action_url="add_cart_item",
    )


def add_header(request):
    return handle_create(
        request=request,
        model=HeaderModel,
        formname=HeaderForm,
        redirect_url="add_header",
        template_url="Dashboard/D_Content/add_header.html",
        action_url="add_header",
    )


def add_otherdetail(request):
    return handle_create(
        request=request,
        model=OtherDetailModel,
        formname=OtherDetailForm,
        redirect_url="add_otherdetail",
        template_url="Dashboard/D_Content/add_otherdet.html",
        action_url="add_otherdetail",
    )


def add_advertisement(request):
    return handle_create(
        request=request,
        model=AdvertisementModel,
        formname=AdvertisementForm,
        redirect_url="add_advertisement",
        template_url="Dashboard/D_Content/add_advertisement.html",
        action_url="add_advertisement",
    )

def add_blog(request):
    return handle_create(
        request=request,
        model=BlogModel,
        formname=BlogForm,
        redirect_url="add_blog",
        template_url="Dashboard/D_Content/add_blog.html",
        action_url="add_blog"
    )

#
#
# Update
def update_product(request, id):
    return handle_update(
        request=request,
        id=id,
        model=ProductModel,
        formname=ProductForm,
        redirect_url="add_product",
        template_url="Dashboard/D_Content/add_product.html",
        action_url="update_product",
    )


def update_category(request, id):
    return handle_update(
        request=request,
        id=id,
        model=CategoryModel,
        formname=CategoryForm,
        redirect_url="add_category",
        template_url="Dashboard/D_Content/add_category.html",
        action_url="update_category",
    )


def update_sub_category(request, id):
    return handle_update(
        request=request,
        id=id,
        model=Sub_CategoryModel,
        formname=SubCategoryForm,
        redirect_url="add_sub_category",
        template_url="Dashboard/D_Content/add_sub_category.html",
        action_url="update_sub_category",
    )


def update_image_slider(request, id):
    return handle_update(
        request=request,
        id=id,
        model=image_SliderModel,
        formname=ImageSliderForm,
        redirect_url="add_image_slider",
        template_url="Dashboard/D_Content/add_image_slider.html",
        action_url="update_image_slider",
    )


def update_cart(request, id):
    return handle_update(
        request=request,
        id=id,
        model=CartModel,
        formname=CartForm,
        redirect_url="add_cart",
        template_url="Dashboard/D_Content/add_cart.html",
        action_url="update_cart",
    )


def update_cart_item(request, id):
    return handle_update(
        request=request,
        id=id,
        model=CartItemModel,
        formname=CartItemForm,
        redirect_url="add_cart_item",
        template_url="Dashboard/D_Content/add_cart_item.html",
        action_url="update_cart_item",
    )


def update_header(request, id):
    return handle_update(
        request=request,
        id=id,
        model=HeaderModel,
        formname=HeaderForm,
        redirect_url="add_header",
        template_url="Dashboard/D_Content/add_header.html",
        action_url="update_header",
    )


def update_otherdetail(request, id):
    return handle_update(
        request=request,
        id=id,
        model=OtherDetailModel,
        formname=OtherDetailForm,
        redirect_url="add_otherdetail",
        template_url="Dashboard/D_Content/add_otherdet.html",
        action_url="update_otherdetail",
    )


def update_advertisement(request, id):
    return handle_update(
        request=request,
        id=id,
        model=AdvertisementModel,
        formname=AdvertisementForm,
        redirect_url="add_advertisement",
        template_url="Dashboard/D_Content/add_advertisement.html",
        action_url="update_advertisement",
    )

def update_blog(request, id):
    return handle_update(
        request=request,
        id=id,
        model=BlogModel,
        formname=BlogForm,
        redirect_url="add_blog",
        template_url="Dashboard/D_Content/add_blog.html",
        action_url="update_blog",
    )


# delete functions
def del_product(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=ProductModel,
        redirect_url="add_product",
        success_msg="Deleted Successfully :)",
    )


def del_category(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=CategoryModel,
        redirect_url="add_category",
        success_msg="Category Deleted Successfully :)",
    )


def del_sub_category(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=Sub_CategoryModel,
        redirect_url="add_sub_category",
        success_msg="Sub Category Deleted Successfully :)",
    )


def del_image_slider(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=image_SliderModel,
        redirect_url="add_image_slider",
        success_msg="Image Slider Deleted Successfully :)",
    )


def del_cart(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=CartModel,
        redirect_url="add_cart",
        success_msg="Cart Deleted Successfully :)",
    )


def del_cart_item(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=CartItemModel,
        redirect_url="add_cart_item",
        success_msg="Cart Item Deleted Successfully :)",
    )


def del_header(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=HeaderModel,  # Assuming the model name is `HeaderModel`
        redirect_url="add_header",
        success_msg="Header Deleted Successfully :)",
    )


def del_otherdetail(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=OtherDetailModel,
        redirect_url="add_otherdetail",
        success_msg="Other Detail Deleted Successfully :)",
    )


def del_advertisement(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=AdvertisementModel,
        redirect_url="add_advertisement",
        success_msg="Advertisement Deleted Successfully :)",
    )

def del_blog(request, id):
    return handle_delete(
        request=request,
        id=id,
        model=BlogModel,
        redirect_url="add_blog",
        success_msg="Blog Deleted Successfully",
    )