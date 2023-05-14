from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("basket/", include("basket.urls", namespace="basket")),
    path("account/", include("account.urls", namespace="account")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("checkout/", include("checkout.urls", namespace="checkout")),
    path("", include("store.urls", namespace="store")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
