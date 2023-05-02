import stripe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from basket.basket import Basket


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

