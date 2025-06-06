from handler.authhandler import *
from .forms import *
from .models import *
from django.contrib.auth.decorators import user_passes_test


def superadmin_required(view_func):
    return user_passes_test(lambda u: u.is_authenticated and u.is_superuser)(view_func)


def create_staff_user_view(request):
    return handling_register(
        request,
        form_class=UserForm,
        model=UserModel,
        templateurl="auth/create_staff.html",
        success_url="dashboard",
        make_staff=True,
    )


@superadmin_required
def create_admin_user_view(request):
    return handling_register(
        request,
        form_class=UserForm,
        model=UserModel,
        templateurl="auth/userregister.html",
        success_url="dashboard",
        make_staff=True,
        make_superuser=True,
    )


def userregister(request):
    return handling_register(
        request=request,
        form_class=UserForm,
        model=UserModel,
        templateurl="auth/userregister.html",
        success_url="userlogin",
    )


def userlogin(request):
    return handling_login(
        request=request,
        model=UserModel,
        templateurl="auth/userlogin.html",
        success_url="mainpage",
    )


def userlogout(request):
    return handling_logout(request=request, model=UserModel, url="userlogin")
