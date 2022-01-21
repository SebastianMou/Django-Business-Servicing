import json

import stripe

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from basket.basket import Basket

# Create your views here.
@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51KFusbLG3Rch548FxCBuH88bWsA2kB3OE261rbEtI0FtiHVrGtZCkMAjkjfJwkqlsCzWfQNxDSQmBzEfawCR6bgg00aWEfvbXH'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/home_payment.html', {'client_secret': intent.client_secret})