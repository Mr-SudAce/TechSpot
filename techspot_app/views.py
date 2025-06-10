from django.shortcuts import *
from .models import *
from .forms import *
from .bot import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.contrib.auth.hashers import *
from django.http import JsonResponse
from handler.authhandler import *
from django.db.models import *
from handler.otherhandler import *


# Create your views here.
# Admin dashboard


from django.shortcuts import render
from django.db.models import Count
from .models import UserModel, ProductModel, OrderItemModel, CategoryModel


def dashboard(request):
    user = UserModel.objects.all()
    product_count = ProductModel.objects.all().count()
    order_count = OrderItemModel.objects.all().count()

    order_data = [order_count] * 12
    product_data = [product_count] * 12

    categories = CategoryModel.objects.annotate(total=Count("productcategory"))
    category_labels = [cat.category_name for cat in categories]
    category_counts = [cat.total for cat in categories]

    color_map = ["#FF0037", "#0099FF", "#FFB700", "#00FF77"]
    category_data = zip(category_labels, category_counts, color_map)

    context = {
        "user": user,
        "productcount": product_count,
        "ordercount": order_count,
        "order_data": order_data,
        "product_data": product_data,
        "category_data": category_data,
    }

    return render(request, "Dashboard/dashboard.html", context)


# User Interface
def mainpage(request):
    redirect_response = check_session_auth(request, 3600)
    if redirect_response:
        return redirect_response

    user_id = request.session.get("user_id")
    user = UserModel.objects.filter(id=user_id).first()

    if not user:
        messages.error(request, "User not found. Please login again.")
        request.session.flush()
        return redirect("userlogin")

    cart = CartModel.objects.filter(user=user, is_paid=False, is_active=True).first()
    if not cart:
        cart = CartModel.objects.create(user=user, is_paid=False, is_active=True)

    cart_items = CartItemModel.objects.filter(cart=cart)

    total_items_count = cart_items.count()
    grand_total = sum(
        float(item.total_price()) if item.product else 0 for item in cart_items
    )

    ############################################ Chat Bot ##########################################
    
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get("prompt", "").strip()
        response = get_bot_response(user_input)

        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "user_input": user_input,
                "response": response,
            })

    ############################################ Chat Bot ##########################################

    context = {
        "user": user,
        "header": HeaderModel.objects.first(),
        "product": ProductModel.objects.all(),
        "image_slider": image_SliderModel.objects.all(),
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
        "otherdetails": OtherDetailModel.objects.first(),
        ############################################ Chat Bot ##########################################
        "response": response,
        "user_input": user_input,
        ############################################ Chat Bot ##########################################
    }

    return render(request, "index.html", context)


def user(request):
    user = UserModel.objects.all()
    context = {"user": user}
    return render(request, "Dashboard/D_Content/user.html", context)


def del_user(request, id):
    user = UserModel.objects.get(id=id)
    user.delete()
    return redirect("user")


# Search
def search_query(request):
    if request.method == "GET":
        query = request.GET.get("search_query", "").strip()
        if query:
            # All items (optional, for display)
            product = ProductModel.objects.all()
            category = CategoryModel.objects.all()
            subcategory = Sub_CategoryModel.objects.all()

            # Direct matches
            queryproducts = ProductModel.objects.filter(
                Q(product_name__icontains=query)
                | Q(product_description__icontains=query)
            )
            querycategory = CategoryModel.objects.filter(category_name__icontains=query)
            querysubcategory = Sub_CategoryModel.objects.filter(
                sub_category_name__icontains=query
            )

            # Products matching category or subcategory
            category_products = ProductModel.objects.filter(
                product_category__in=querycategory
            )
            subcategory_products = ProductModel.objects.filter(
                pro_sub_category__in=querysubcategory
            )

            # Combine all product querysets without duplicates
            all_query_products = (
                queryproducts | category_products | subcategory_products
            ).distinct()

            context = {
                "queryproducts": all_query_products,
                "querycategory": querycategory,
                "querysubcategory": querysubcategory,
                "product": product,
                "category": category,
                "subcategory": subcategory,
                "query": query,
            }
            return render(request, "content/search.html", context)
        else:
            return render(
                request, "content/search.html", {"error": "Please enter a search query"}
            )
    else:
        return redirect("mainpage")


# Cart Detail
def cart_detail(request):
    cart_det = CartItemModel.objects.all()

    user_id = request.session.get("user.id")
    user = UserModel.objects.filter(id=user_id).first()

    if user_id:
        cart = CartModel.objects.get(user=user, is_paid=False).first()
        cart_items = CartItemModel.objects.filter(cart=cart) if cart else []
    else:
        cart_items = []

    # total_items_count = cart_items.count()
    total_items_count = (
        len(cart_items) if isinstance(cart_items, list) else cart_items.count()
    )
    grand_total = sum(
        float(item.total_price()) if item.product else 0 for item in cart_items
    )
    context = {
        "cartdet": cart_det,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
    }
    return render(request, "content/cart_detail.html", context)


# update_all_cart_details
def update_all_cart_details(request):
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("quantity_"):
                cart_item_id = key.split("_")[1]
                quantity = int(value)
                cart_item = get_object_or_404(CartItemModel, id=cart_item_id)
                cart_item.quantity = quantity
                cart_item.total_price = cart_item.product.product_price * quantity
                cart_item.save()

        return redirect("cart_Detail")


def get_common_context(request, products=None, extra_context=None):
    categories = CategoryModel.objects.prefetch_related("subcategories").all()
    sub_categories = Sub_CategoryModel.objects.all()
    sliders = image_SliderModel.objects.all()
    header = HeaderModel.objects.last()
    otherdetails = OtherDetailModel.objects.last()
    advertisement = AdvertisementModel.objects.all()
    allcategory = CategoryModel.objects.all()

    user_id = request.session.get("user_id")
    cart_items = []
    try:
        if user_id:
            custom_user = UserModel.objects.get(id=user_id)
            # Check if user is active
            if not custom_user.is_active:
                request.session.flush()
                return redirect("login")

            # Fetch unpaid cart
            cart = CartModel.objects.filter(user=custom_user.id, is_paid=False).first()
            if cart:
                cart_items = CartItemModel.objects.filter(cart=cart)

    except UserModel.DoesNotExist:
        request.session.flush()
        return redirect("userlogin")

    cart_items = [item for item in cart_items if item.product]
    total_items_count = len(cart_items)
    grand_total = sum(float(item.total_price()) for item in cart_items)

    context = {
        "categories": categories,
        "sub_categories": sub_categories,
        "images": sliders,
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
        "header": header,
        "otherdetails": otherdetails,
        "advertisement": advertisement,
        "allcategory": allcategory,
    }

    if products is not None:
        context["products"] = products

    if extra_context:
        context.update(extra_context)

    return context


# filter products by category -> subcategory
def filter_by_subcategory(request, id):
    if not request.session.get("user_id"):
        return redirect("login")
    fltr_subcategory = get_object_or_404(Sub_CategoryModel, id=id)
    products = ProductModel.objects.filter(pro_sub_category=fltr_subcategory)
    context = get_common_context(
        request, products=products, extra_context={"fltr_subcategory": fltr_subcategory}
    )
    return render(request, "content/cards.html", context)


# filter products by category
def filter_by_category(request, id):
    if not request.session.get("user_id"):
        return redirect("login")
    fltr_category = get_object_or_404(CategoryModel, id=id)
    products = ProductModel.objects.filter(product_category=fltr_category)
    context = get_common_context(
        request, products=products, extra_context={"fltr_category": fltr_category}
    )
    return render(request, "content/cards.html", context)


# Show all products
def show_allproducts(request, category_id=None):
    if not request.session.get("user_id"):
        return redirect("login")
    if category_id:
        fltr_category = get_object_or_404(CategoryModel, id=category_id)
        products = ProductModel.objects.filter(product_category=fltr_category)
        extra_context = {"fltr_category": fltr_category}
    else:
        products = ProductModel.objects.all()
        extra_context = {}

    context = get_common_context(
        request, products=products, extra_context=extra_context
    )
    return render(request, "content/cards.html", context)


# add to cart
def add_to_cart(request, id):
    product = get_object_or_404(ProductModel, id=id)

    userid = request.session.get("user_id")
    if userid:
        cart = CartModel.objects.filter(
            user_id=userid, is_paid=False, is_active=True
        ).first()
        if not cart:
            cart = CartModel.objects.create(
                user_id=userid, is_paid=False, is_active=True
            )
        cart_item = CartItemModel.objects.filter(cart=cart, product=product).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItemModel.objects.create(cart=cart, product=product, quantity=1)
        return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        cart = request.session.get("cart", {})
        if str(id) in cart:
            cart[str(id)]["quantity"] += 1
        else:
            cart[str(id)] = {
                "product_id": id,
                "quantity": 1,
            }
        request.session["cart"] = cart
        return redirect(request.META.get("HTTP_REFERER", "/"))


# delete cart item
def delete_cart_item(request, id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItemModel, id=id)
        cart_item.delete()
        return redirect(request.META.get("HTTP_REFERER", "/"))


# delete cartdetail item
def cartdetail_delete(request, cart_det_id):
    try:
        cart_item = get_object_or_404(CartItemModel, id=cart_det_id)
        cart_item.delete()
        return redirect("cart_Detail")
    except CartItemModel.DoesNotExist:
        return HttpResponse("Cart item not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


# update cart quantity
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


# checkout
@transaction.atomic
def checkout(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("login")  # Fallback if user_id isn't in session

    custom_user = get_object_or_404(UserModel, id=user_id)
    cart = CartModel.objects.filter(user=custom_user.id, is_active=True).first()

    if not cart:
        return redirect("cart_Detail")

    cart_items = CartItemModel.objects.filter(cart=cart)
    if not cart_items.exists():
        return redirect("cart_Detail")

    total_price = sum(
        float(item.product.product_price) * item.quantity for item in cart_items
    )

    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user = custom_user
            try:
                shipping.save()  # ✅ Must succeed before using in Order
            except Exception as e:
                messages.error(request, "Failed to save shipping info.")
                return redirect("checkout")

            # Create the order
            order = OrderModel.objects.create(
                user=custom_user,
                shipping_info=shipping,
                total_price=total_price,
                payment_method="COD",
                status="Confirmed",
            )

            # Create order items and update stock
            for item in cart_items:
                if not item.product:
                    return redirect("cart_Detail")
                OrderItemModel.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.product_price,
                )
                item.product.product_stock -= item.quantity
                item.product.save()

            # Clear cart
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


# productDetail
def product_itemView_detail(request, id):
    product_itemView_detail = ProductModel.objects.get(id=id)
    products = ProductModel.objects.exclude(id=id)
    cart_itm = CartItemModel.objects.all()
    header = HeaderModel.objects.last()

    cart = CartModel.objects.filter(
        user=request.session.get("user_id"), is_paid=False
    ).first()
    product_in_cart = False
    if cart:
        product_in_cart = CartItemModel.objects.filter(
            cart=cart, product=product_itemView_detail
        ).exists()

    context = {
        "product_detailV": product_itemView_detail,
        "product_in_cart": product_in_cart,
        "similarproduct": products,
        "header": header,
        "cart_itm": cart_itm,
    }
    return render(request, "content/product_detail.html", context)


##################################  CHATBOT #######################################

# def bot_view(request):
#     response = ""
#     user_input = ""

#     if request.method == "POST":
#         user_input = request.POST.get("prompt", "").strip().lower()
#         print("🗣️ User said:", user_input)
#         if user_input:
#             if user_input in ["hello", "hi", "hey"]:
#                 jokes = [
#                     "Why don’t skeletons fight each other? They don’t have the guts.",
#                     "Parallel lines have so much in common. It’s a shame they’ll never meet.",
#                     "I told my wife she was drawing her eyebrows too high. She looked surprised.",
#                 ]
#                 response = random.choice(jokes)
#             else:
#                 response = "Not Found !!!!!"
#         else:
#             response = "Please Say Something :D"
#         print("🤖 Bot responded:", response)

#     context = {
#         "response": response,
#         "user_input": user_input
#     }

#     return render(request, "bot.html", context)


##################################  CHATBOT #######################################
