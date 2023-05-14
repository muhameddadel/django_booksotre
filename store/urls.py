from django.urls import path

from .views import *

app_name = "store"

urlpatterns = [
    path("", all_products, name="all-products"),
    path("<slug:slug>/", product_detail, name="product-detail"),
    path("shop/<slug:category_slug>/", category_list, name="category-list"),
]
