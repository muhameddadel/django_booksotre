from django.urls import path

from .views import *

app_name = 'payment'


urlpatterns = [
    path('', BasketView, name='basket'),
    path('orderplaced/', order_placed, name='order_placed'),
    path('webhook/', stripe_webhook, name='order_placed'),
]
