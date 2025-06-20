from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.hashers import *
from django.db.models import Q, Count
from .models import *
from .forms import *
from .bot import get_bot_response
from handler.authhandler import check_session_auth
from handler.otherhandler import *
from handler.getcartshandler import *
from techspot_app.context_processors import get_common_context


# 🧠 Dashboard View
def dashboard(request):
    users = UserModel.objects.all()
    product_count = ProductModel.objects.count()
    order_count = OrderItemModel.objects.count()

    category_qs = CategoryModel.objects.annotate(total=Count("productcategory"))
    labels = [cat.category_name for cat in category_qs]
    counts = [cat.total for cat in category_qs]
    color_map = ["#FF0037", "#0099FF", "#FFB700", "#00FF77"]

    context = {
        "user": users,
        "productcount": product_count,
        "ordercount": order_count,
        "header": HeaderModel.objects.all(),
        "order_data": [order_count] * 12,
        "product_data": [product_count] * 12,
        "category_data": zip(labels, counts, color_map),
    }

    return render(request, "Dashboard/dashboard.html", context)


# 🏠 Main Page with Chatbot + Cart Context
def mainpage(request):
    redirect_response = check_session_auth(request, 3600)
    if redirect_response:
        return redirect_response

    user, cart_items, total_items_count, grand_total = get_cart_context(request)

    if not user:
        messages.error(request, "User not found. Please login again.")
        request.session.flush()
        return redirect("userlogin")

    response = user_input = ""
    if request.method == "POST":
        user_input = request.POST.get("prompt", "").strip()
        response = get_bot_response(user_input)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"user_input": user_input, "response": response})

    context = {
        "user": user,
        "header": HeaderModel.objects.first(),
        "product": ProductModel.objects.all(),
        "image_slider": image_SliderModel.objects.all(),
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
        "otherdetails": OtherDetailModel.objects.first(),
        "response": response,
        "user_input": user_input,
    }

    return render(request, "index.html", context)


def user(request):
    return render(
        request, "Dashboard/D_Content/user.html", {"user": UserModel.objects.all()}
    )


def del_user(request, id):
    get_object_or_404(UserModel, id=id).delete()
    return redirect("user")


# 🔍 Search
def search_query(request):
    if request.method == "GET":
        query = request.GET.get("search_query", "").strip()
        if query:
            queryproducts = ProductModel.objects.filter(
                Q(product_name__icontains=query)
                | Q(product_description__icontains=query)
            )
            querycategory = CategoryModel.objects.filter(category_name__icontains=query)
            querysubcategory = Sub_CategoryModel.objects.filter(
                sub_category_name__icontains=query
            )

            all_query_products = (
                queryproducts
                | ProductModel.objects.filter(product_category__in=querycategory)
                | ProductModel.objects.filter(pro_sub_category__in=querysubcategory)
            ).distinct()

            context = {
                "queryproducts": all_query_products,
                "querycategory": querycategory,
                "querysubcategory": querysubcategory,
                "product": ProductModel.objects.all(),
                "category": CategoryModel.objects.all(),
                "subcategory": Sub_CategoryModel.objects.all(),
                "query": query,
            }
            return render(request, "content/searchedItems.html", context)
        return render(
            request, "content/searchedItems.html", {"error": "Please enter a search query"}
        )
    return redirect("mainpage")


# 🛒 Cart Detail
def cart_detail(request):
    _, cart_items, total_items_count, grand_total = get_cart_context(request)
    return render(
        request,
        "content/cart_detail.html",
        {
            "cartdet": cart_items,
            "total_items_count": total_items_count,
            "grand_total": grand_total,
        },
    )


def update_all_cart_details(request):
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("quantity_"):
                cart_item_id = key.split("_")[1]
                cart_item = get_object_or_404(CartItemModel, id=cart_item_id)
                cart_item.quantity = int(value)
                cart_item.total_price = (
                    cart_item.product.product_price * cart_item.quantity
                )
                cart_item.save()
    return redirect("cart_Detail")


# 🔎 Filter by Subcategory
def filter_by_subcategory(request, id):
    if not request.session.get("user_id"):
        return redirect("userlogin")
    fltr_subcategory = get_object_or_404(Sub_CategoryModel, id=id)
    products = ProductModel.objects.filter(pro_sub_category=fltr_subcategory)
    return render(
        request,
        "content/cards.html",
        get_common_context(request, products, {"fltr_subcategory": fltr_subcategory}),
    )


def filter_by_category(request, id):
    if not request.session.get("user_id"):
        return redirect("userlogin")
    fltr_category = get_object_or_404(CategoryModel, id=id)
    products = ProductModel.objects.filter(product_category=fltr_category)
    return render(
        request,
        "content/cards.html",
        get_common_context(request, products, {"fltr_category": fltr_category}),
    )


def show_allproducts(request, category_id=None):
    if not request.session.get("user_id"):
        return redirect("userlogin")

    if category_id:
        fltr_category = get_object_or_404(CategoryModel, id=category_id)
        products = ProductModel.objects.filter(product_category=fltr_category)
        extra_context = {"fltr_category": fltr_category}
    else:
        products = ProductModel.objects.all()
        extra_context = {}

    return render(
        request,
        "content/cards.html",
        get_common_context(request, products, extra_context),
    )


def add_to_cart(request, id):
    product = get_object_or_404(ProductModel, id=id)
    user_id = request.session.get("user_id")

    if user_id:
        cart, _ = CartModel.objects.get_or_create(
            user_id=user_id, is_paid=False, is_active=True
        )
        cart_item, created = CartItemModel.objects.get_or_create(
            cart=cart, product=product
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        cart = request.session.get("cart", {})
        if str(id) in cart:
            cart[str(id)]["quantity"] += 1
        else:
            cart[str(id)] = {"product_id": id, "quantity": 1}
        request.session["cart"] = cart

    return redirect(request.META.get("HTTP_REFERER", "/"))


def delete_cart_item(request, id):
    if request.method == "POST":
        get_object_or_404(CartItemModel, id=id).delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


def cartdetail_delete(request, cart_det_id):
    try:
        get_object_or_404(CartItemModel, id=cart_det_id).delete()
        return redirect("cart_Detail")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


def update_cart_quantity(request, id):
    product = get_object_or_404(ProductModel, id=id)
    user_id = request.session.get("user_id")
    cart = CartModel.objects.filter(user=user_id, is_paid=False).first()

    if cart:
        cart_item = CartItemModel.objects.filter(cart=cart, product=product).first()
        if cart_item:
            quantity = int(request.POST.get("quantity", 1))
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            return redirect("product_itemView_detail", id=id)


@transaction.atomic
def checkout(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")

    user = get_object_or_404(UserModel, id=user_id)
    cart = CartModel.objects.filter(user=user, is_active=True).first()

    if not cart:
        return redirect("cart_Detail")

    cart_items = CartItemModel.objects.filter(cart=cart)
    if not cart_items.exists():
        return redirect("cart_Detail")

    total_price = sum(item.product.product_price * item.quantity for item in cart_items)

    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user = user
            shipping.save()

            order = OrderModel.objects.create(
                user=user,
                shipping_info=shipping,
                total_price=total_price,
                payment_method="COD",
                status="Confirmed",
            )

            for item in cart_items:
                OrderItemModel.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price,
                )
                item.product.product_stock -= item.quantity
                item.product.save()

            cart.is_active = False
            cart.save()
            cart_items.delete()

            return redirect("order_success", order_id=order.id)
    else:
        form = ShippingForm()

    return render(
        request,
        "content/checkout.html",
        {"form": form, "cart_items": cart_items, "total_price": total_price},
    )


def order_success(request, order_id):
    order = get_object_or_404(
        OrderModel, id=order_id, user=request.session.get("user_id")
    )
    return render(request, "content/order_success.html", {"order": order})


def product_itemView_detail(request, id):
    product = get_object_or_404(ProductModel, id=id)
    similarproduct = ProductModel.objects.filter(
        product_category=product.product_category
    ).exclude(id=id)

    cart = CartModel.objects.filter(
        user=request.session.get("user_id"), is_paid=False
    ).first()
    product_in_cart = False
    if cart:
        product_in_cart = CartItemModel.objects.filter(
            cart=cart, product=product
        ).exists()

    return render(
        request,
        "content/product_detail.html",
        {
            "product_detailV": product,
            "product_in_cart": product_in_cart,
            "similarproduct": similarproduct,
            "header": HeaderModel.objects.last(),
            "cart_itm": CartItemModel.objects.all(),
        },
    )


# 📰 Blog Views
def blog_detail(request, slug):
    return render(
        request,
        "content/blog_detail.html",
        {"blog": get_object_or_404(BlogModel, slug=slug)},
    )


def blogs(request):
    return render(request, "content/blog.html", {"blogs": BlogModel.objects.all()})
