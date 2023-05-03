import stripe
import json

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from basket.basket import Basket
from orders.views import payment_confirmation


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    
    stripe.api_key = 'sk_test_51N3ElZHCEFgrfiGmEfrNWjSLGSnLzUKzuZW24hAFswSlAfuIW0DFnKT8i6zbHObHZALyyPGddwc8K8MQyWTwF3jk00JUBvFC1C'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    context = {'client_secret': intent.client_secret}
    return render(request, 'payment/home.html', context)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try: 
        event = stripe.Event.construct_from(json.loads(payload), stripe.api_key)
    except ValueError:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_confirmation(event.data.object.client_secret)
    else:
        print(f'Unhandled event type{event.type}')

    return HttpResponse(status=200)


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')