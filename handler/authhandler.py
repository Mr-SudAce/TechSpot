from django.contrib import messages
from django.contrib.auth.hashers import *
from datetime import datetime
from django.shortcuts import render, redirect


# For handling registration
# This function handles the registration process for users.
def handling_register(request, form_class, model, templateurl, success_url, make_staff=False, make_superuser=False):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            # model field
            number = form.cleaned_data.get("number")
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            if not number or len(str(number)) < 8 or len(str(number)) > 10:
                messages.error(request, "Number should be 8-10 digits")
                return render(request, templateurl, {"form": form})

            if not password or len(password) < 8:
                messages.error(request, "Password should be at least 8 characters long")
                return render(request, templateurl, {"form": form})

            if model.objects.filter(number=number).exists():
                messages.error(request, f"The number {number} is already registered")
                return render(request, templateurl, {"form": form})

            if model.objects.filter(email=email).exists():
                messages.error(request, f"Email {email} already exists")
                return render(request, templateurl, {"form": form})

            user = form.save(commit=False)
            user.password = make_password(password)
            # NEW: Add role flags based on function parameters
            user.is_staff = make_staff
            user.is_superuser = make_superuser
            user.is_active = True
            user.save()

            messages.success(request, f"Account Created for {username}")
            return redirect(success_url)
        else:
            messages.error(request, "Fix errors in the form below.")
    else:
        form = form_class()

    return render(request, templateurl, {"form": form})


# For handling login
# This function handles the login process for users.
def handling_login(request, model, templateurl, success_url):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = model.objects.filter(email=email).first()
        if user and check_password(password, user.password):
            request.session["user_id"] = user.id
            request.session["is_authenticated"] = True
            messages.success(request, f"Welcome {user.username}")
            return redirect(success_url)
        else:
            messages.error(request, "Invalid email or password")
    return render(request, templateurl)


# For handling logout
def handling_logout(request, id=None, model=None, url=None):
    # If id not passed, get from session
    if id is None:
        id = request.session.get("user_id")

    if id is None or model is None or url is None:
        messages.error(request, "Invalid logout request.")
        request.session.flush()
        return redirect("userlogin")

    user = model.objects.filter(id=id).first()
    if user:
        messages.success(request, f"Goodbye {user.username}")
    else:
        messages.error(request, "User not found. Please login again.")

    request.session.flush()
    return redirect(url)


def get_time_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 21:
        return "Good Evening"
    else:
        return "Good Night"


def check_session_auth(request, timer):
    if not request.session.get("is_authenticated"):
        messages.error(request, "Please login to continue")
        return redirect("userlogin")

    request.session.set_expiry(timer)  # session expires on browser close
    return None
