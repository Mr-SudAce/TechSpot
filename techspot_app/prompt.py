def ecommerce_prompts(user_input):
    user_input = user_input.strip().lower()

    if user_input in ["shipping", "order", "where is my order", "order status"]:
        return "Tracking your package like a detective on a hot trail 🔎. Just kidding, your order’s on the way! Check your email for updates 📦."

    elif user_input in ["return", "refund", "how to return"]:
        return "Changed your mind? No worries — returns are easier than finding a 'free shipping' deal around here. Just visit your orders page and follow the return instructions!"

    elif user_input in ["discount", "promo", "coupon"]:
        return "Looking for some sweet deals? 🎉 Use code SAVE10 at checkout for 10% off! Because who doesn’t love saving cash?"

    elif user_input in ["payment methods", "how to pay", "payment options"]:
        return "We accept all the classics: credit card, debit card, PayPal, and even carrier pigeons (just kidding, not really). Pick what suits you best!"

    elif user_input in ["support", "help", "customer service"]:
        return "Need help? Our support squad is standing by like superheroes in hoodies 🦸‍♂️. Hit us up anytime!"

    elif user_input in ["recommend", "suggest", "what should i buy"]:
        return "Looking for recommendations? Based on your style, you might love these trending picks 🔥. Wanna see some cool stuff?"

    elif user_input in ["new arrivals", "latest products"]:
        return "Fresh drops just landed! Check out the new arrivals before everyone else grabs ‘em 🛍️."

    elif user_input in ["cart", "my cart", "view cart"]:
        return "Your cart’s waiting for you like a loyal puppy 🐶. Ready to check out or wanna add more goodies?"

    elif user_input in ["order cancel", "cancel order"]:
        return "Changed your mind? Orders can be canceled within 1 hour of purchase — just let us know ASAP ⏳."

    elif user_input in ["gift", "gift wrap"]:
        return "Want your order gift-wrapped? We got you covered with fancy paper and a bow 🎁. Just add the gift option at checkout!"

    else:
        return None
