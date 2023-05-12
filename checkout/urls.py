from django.urls import path

from .views import *

app_name = 'checkout'

urlpatterns = [
    path("deliverychoices", deliverychoices, name="deliverychoices"),
    path("basket_update_delivery/", basket_update_delivery, name="basket_update_delivery"),
]
