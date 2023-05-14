from django.urls import path

from .views import *

app_name = "basket"

urlpatterns = [
    path("", basket_summary, name="basket-summary"),
    path("add/", basket_add, name="basket-add"),
    path("delete/", basket_delete, name="basket-delete"),
    path("update/", basket_update, name="basket-update"),
]
