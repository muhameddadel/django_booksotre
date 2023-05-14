from django.contrib.auth import views
from django.urls import path
from django.views.generic import TemplateView

from .forms import *
from .views import *

app_name = "account"

urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(
            template_name="account/login.html", form_class=UserLoginForm
        ),
        name="login",
    ),
    path(
        "logout/", views.LogoutView.as_view(next_page="/account/login/"), name="logout"
    ),
    path("register/", account_register, name="register"),
    path("activate/<slug:uidb64>/<slug:token>", account_activate, name="activate"),
    path(
        "password_reset/",
        views.PasswordResetView.as_view(
            template_name="account/password_reset/password_reset_form.html",
            success_url="password_reset_email_confirm",
            email_template_name="account/user/password_reset_email.html",
            form_class=PwdResetForm,
        ),
        name="pwdreset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset/password_reset_confirm.html",
            success_url="account/password_reset_complete/",
            form_class=PwdResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/password_reset_email_confirm/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset_complete/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_complete",
    ),
    # dashboard
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/edit/", edit_details, name="edit_details"),
    path("profile/delete_user/", delete_user, name="delete_user"),
    path(
        "profile/delete_cofirm/",
        TemplateView.as_view(template_name="account/dashboard/delete_confirm.html"),
        name="delete_confirmation",
    ),
    # addresses
    path("addresses/", view_address, name="addresses"),
    path("add_address/", add_address, name="add_address"),
    path("addresses/edit/<slug:id>/", edit_address, name="edit_address"),
    path("addresses/delete/<slug:id>/", delete_address, name="delete_address"),
    path("addresses/set_default/<slug:id>/", set_default, name="set_defualt"),
    path("user_orders/", user_orders, name="user_orders"),
    # wishlist
    path("wishlist/", wishlist, name="wishlist"),
    path("wishlist/add_to_wishlist/<int:id>/", add_to_wishlist, name="add_to_wishlist"),
]
