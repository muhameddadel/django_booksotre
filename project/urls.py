from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls', namespace='basket')),
    path('acount/', include('basket.urls', namespace='account')),
    path('', include('store.urls', namespace='store')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)