import os
from django.contrib.auth.decorators import *
from django.contrib.auth import *
from django.contrib.auth.forms import *
from django.contrib import messages
from django.shortcuts import *
from django.conf import settings
from .models import *
from .forms import *


# Create your views here.


# Authentication
# Login view
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")  # Redirect if already logged in

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "/")
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, "User_Authentication/userlogin.html", {"form": form})


# Registration view
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been created! You can log in now."
            )
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "User_Authentication/userregister.html", {"form": form})


# Logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect("/")


# Example of a view that requires the user to be logged in


# Home
@login_required
def home(request):
    category = Category.objects.all()
    sub_category = Sub_Category.objects.all()
    sliders = image_Slider.objects.all()
    product = Product.objects.all()
    header = Header.objects.last()
    otherdetails = OtherDetail.objects.last()

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_paid=False).first()
        cart_items = CartItem.objects.filter(cart=cart) if cart else []
    else:
        cart_items = []

    # total_items_count = cart_items.count()
    total_items_count = (
        len(cart_items) if isinstance(cart_items, list) else cart_items.count()
    )
    grand_total = sum(item.total_price() for item in cart_items)

    context = {
        "categories": category,
        "sub_categories": sub_category,
        "images": sliders,
        "product": product,
        "cart_item": cart_items,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
        "header": header,
        "otherdetails": otherdetails,
    }
    return render(request, "home.html", context)


def shop(request):
    shop_products = Product.objects.all()
    context = {
        "shop_products": shop_products,
    }
    return render(request, "content/shop.html", context)


def tele_shopping_nepal(request):
    tele_category = Category.objects.filter(
        category_name="Tele-Shopping"
    ).prefetch_related("productcategory")
    context = {
        "tele_category": tele_category,
    }
    return render(request, "content/tele_shopping_nepal.html", context)


def gym(request):
    gym_category = Category.objects.filter(category_name="GYM").prefetch_related(
        "productcategory"
    )

    context = {
        "gym_category": gym_category,
    }
    return render(request, "content/gym.html", context)


def gaming(request):
    gaming_category = Category.objects.filter(
        category_name="Gaming & Accessories"
    ).prefetch_related("productcategory")
    context = {
        "gaming_category": gaming_category,
    }
    return render(request, "content/gaming.html", context)


def contact_us(request):
    return render(request, "content/contactus.html")


# add to cart
@login_required
def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user, is_paid=False)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=1)

    else:
        cart = request.session.get("cart", {})

        if str(id) in cart:
            cart[str(id)]["quantity"] += 0
        else:
            cart[str(id)] = {
                "product_id": id,
                "quantity": 1,
            }
        request.session["cart"] = cart
    return redirect("home")

# add to car
def delete_cart_item(request, cart_item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()
        return redirect("/")


def cartdetail_delete(request, cart_det_id):
    try:
        cart_item = get_object_or_404(CartItem, id=cart_det_id)
        cart_item.delete()
        return redirect("cart_Detail")
    except CartItem.DoesNotExist:
        return HttpResponse("Cart item not found.", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


# cart_detail
def cart_detail(request):
    cart_det = CartItem.objects.all()

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, is_paid=False).first()
        cart_items = CartItem.objects.filter(cart=cart) if cart else []
    else:
        cart_items = []

    # total_items_count = cart_items.count()
    total_items_count = (
        len(cart_items) if isinstance(cart_items, list) else cart_items.count()
    )
    grand_total = sum(item.total_price() for item in cart_items)
    context = {
        "cartdet": cart_det,
        "total_items_count": total_items_count,
        "grand_total": grand_total,
    }
    return render(request, "content/cart_detail.html", context)


def update_all_cart_details(request):
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith("quantity_"):
                cart_item_id = key.split("_")[1]
                quantity = int(value)
                cart_item = get_object_or_404(CartItem, id=cart_item_id)
                cart_item.quantity = quantity
                cart_item.total_price = cart_item.product.product_price * quantity
                cart_item.save()

        return redirect("cart_Detail")


def search_query(request):
    if request.method == "GET":
        query = request.GET.get("search_query", "").strip()
        if query:
            product = Product.objects.all()
            products = Product.objects.filter(product_name__icontains=query)
            context = {"products": products, "product": product, "query": query}
            return render(request, "content/search.html", context)
        else:
            return render(
                request, "content/search.html", {"error": "Please enter a search query"}
            )
    else:
        return redirect("home")


# productDetail
def product_itemView_detail(request, id):
    product_itemView_detail = Product.objects.get(id=id)
    products = Product.objects.all()
    cart_itm = CartItem.objects.all()
    cart = Cart.objects.get(user=request.user)
    product_in_cart = CartItem.objects.filter(
        cart=cart, product=product_itemView_detail
    ).exists()
    context = {
        "product_detailV": product_itemView_detail,
        "product_in_cart": product_in_cart,
        "products": products,
        "cart_itm": cart_itm,
    }
    return render(request, "content/product_detail.html", context)


def update_cart_quantity(request, id):
    product = get_object_or_404(Product, id=id)
    cart = Cart.objects.filter(user=request.user, is_paid=False).first()

    if cart:
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            quantity = int(request.POST.get("quantity", 1))
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            return redirect("product_itemView_detail", id=id)


# Dashboard
def dashboard(request):

    return render(request, "Dashboard/dashboard.html")


# Dashboard > D_Content
def add_product(request):
    product = Product.objects.order_by('-id')
    A_product = AddProductView()
    if request.method == "POST":
        if "submit_A_product" in request.POST:
            A_product = AddProductView(request.POST, request.FILES)
            if A_product.is_valid():
                A_product.save()
                return redirect("add_product")
    context = {"A_product": A_product, "product": product}
    return render(request, "Dashboard/D_Content/add_product.html", context)


def add_category(request):
    category = Category.objects.all()
    A_category = AddCategoryView()
    if request.method == "POST":
        if "submit_A_category" in request.POST:
            A_category = AddCategoryView(request.POST, request.FILES)
            if A_category.is_valid():
                A_category.save()
                return redirect("add_category")
    context = {"A_category": A_category, "category": category}
    return render(request, "Dashboard/D_Content/add_category.html", context)


def add_sub_category(request):
    A_sub_category = AddSub_CategoryView()
    if request.method == "POST":
        if "submit_A_sub_category" in request.POST:
            A_sub_category = AddSub_CategoryView(request.POST, request.FILES)
            if A_sub_category.is_valid():
                A_sub_category.save()
                return redirect("add_sub_category")
    context = {"A_sub_category": A_sub_category}
    return render(request, "Dashboard/D_Content/add_sub_category.html", context)


def add_image_slider(request):
    A_Image_slider = AddImageSliderView()
    if request.method == "POST":
        if "submit_A_image_slider" in request.POST:
            A_Image_slider = AddImageSliderView(request.POST, request.FILES)
            if A_Image_slider.is_valid():
                A_Image_slider.save()
                return redirect("add_image_slider")
    context = {"A_Image_slider": A_Image_slider}
    return render(request, "Dashboard/D_Content/add_image_slider.html", context)


def add_cart(request):
    A_cart = AddCartView()
    if request.method == "POST":
        if "submit_A_cart" in request.POST:
            A_cart = AddCartView(request.POST, request.FILES)
            if A_cart.is_valid():
                A_cart.save()
                return redirect("add_cart")
    context = {"A_cart": A_cart}
    return render(request, "Dashboard/D_Content/add_cart.html", context)


def add_cart_item(request):
    A_cat_item = AddCartItemView()
    if request.method == "POST":
        if "submit_A_cat_item" in request.POST:
            A_cat_item = AddCartItemView(request.POST, request.FILES)
            if A_cat_item.is_valid():
                A_cat_item.save()
                return redirect("add_cart_item")
    context = {"A_cat_item": A_cat_item}
    return render(request, "Dashboard/D_Content/add_cart_item.html", context)


# header
def add_header_mid(request):
    header = Header.objects.last()
    if request.method == "POST":
        if "submit_A_header_mid_save" in request.POST:
            A_header_mid = HeaderView(request.POST, request.FILES)
            if A_header_mid.is_valid():
                A_header_mid.save()
                return redirect("add_header_mid")
    else:
        # Initialize the form for GET request
        A_header_mid = HeaderView()

    context = {"A_header_mid": A_header_mid, "header": header}
    return render(request, "Dashboard/D_Content/add_header_mid.html", context)


def add_otherdetail(request):
    otherdetails = OtherDetail.objects.last()
    if request.method == "POST":
        if "submit_A_otherdetails_save" in request.POST:
            A_otherdetails = OtherdetailsView(request.POST, request.FILES)
            if A_otherdetails.is_valid():
                A_otherdetails.save()
                return redirect("add_otherdetail")
    else:
        # Initialize the form for GET request
        A_otherdetails = OtherdetailsView()
    context = {"A_otherdetails": A_otherdetails, "otherdetails": otherdetails}
    return render(request, "Dashboard/D_Content/add_otherdet.html", context)




# delete functions
def del_otherdetail(request, id):
    otherdetail = get_object_or_404(OtherDetail, id=id)
    otherdetail.delete()
    messages.success(request, "Other Detail deleted successfully.")
    return redirect("add_otherdetail")
def del_header(request, id):
    header = get_object_or_404(Header, id=id)
    header.delete()
    messages.success(request, "Header deleted successfully.")
    return redirect("add_header_mid")

def del_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect("add_product")

def del_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, "Category deleted successfully.")
    return redirect("add_category")

def del_sub_category(request, id):
    sub_category = get_object_or_404(Sub_Category, id=id)
    sub_category.delete()
    messages.success(request, "Sub-Category deleted successfully.")
    return redirect("add_sub_category")

def del_image_slider(request, id):
    image_slider = get_object_or_404(image_Slider, id=id)
    image_slider.delete()
    messages.success(request, "Image Slider deleted successfully.")
    return redirect("add_image_slider")

def del_cart(request, id):
    cart = get_object_or_404(Cart, id=id)
    cart.delete()
    messages.success(request, "Cart deleted successfully.")
    return redirect("add_cart")

def del_cart_item(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()
    messages.success(request, "Cart Item deleted successfully.")
    return redirect("add_cart_item")

























# pages
def new_user_guide(request):
    return render(request, "Pages/new_user_guide.html")


def shipping_charges(request):
    return render(request, "Pages/shipping_charges.html")


def delivery_timeline(request):
    return render(request, "Pages/delivery_timeline.html")


def order_tracking(request):
    return render(request, "Pages/order_tracking.html")


def canceling_order(request):
    return render(request, "Pages/canceling_order.html")


def return_product(request):
    return render(request, "Pages/return_product.html")


def return_refund(request):
    return render(request, "Pages/return_refund.html")


def faq(request):
    return render(request, "Pages/FAQ.html")


def checkout(request):
    return render(request, "Pages/checkout.html")


def terms_and_condition(request):
    return render(request, "Pages/terms_and_condition.html")


def my_orders(request):
    return render(request, "Pages/my_orders.html")


def blog(request):
    return render(request, "Pages/blog.html")
