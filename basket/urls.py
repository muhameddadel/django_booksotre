from django.urls import path

from .views import *

app_name = 'basket'

urlpatterns = [
    path('', basket_summary, name='basket-summary'),
    path('', basket_add, name='basket-add'),
]
