from django.urls import path

from .views import *

app_name = 'payment'


urlpatterns = [
    path('', BasketView, name='basket'),
]
