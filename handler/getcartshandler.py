
from techspot_app.models import *







def get_cart_context(request):
    user_id = request.session.get("user_id")
    cart_items, total_items_count, grand_total = [], 0, 0.0
    user = None

    if user_id:
        user = UserModel.objects.filter(id=user_id).first()
        if user:
            cart = CartModel.objects.filter(user=user, is_paid=False, is_active=True).first()
            if cart:
                cart_items = CartItemModel.objects.filter(cart=cart, product__isnull=False)
                total_items_count = cart_items.count()
                grand_total = sum(float(item.total_price()) for item in cart_items)

    return user, cart_items, total_items_count, grand_total
