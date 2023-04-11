from django.urls import path
from .views import *


app_name = 'store'

urlpatterns = [
    path('', all_products, name='all-products'),
]
