import stripe
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from pay_system.models import Item

stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://127.0.0.1:8000'

class BuyProduct(View):

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                        'price_data': {
                                'currency': 'usd',
                                'product_data': {
                                        'name': item.name,
                                },
                                'unit_amount': item.get_price_int(),
                        },
                        'quantity': 1,
                }],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return JsonResponse({'id': session.id})


class ItemList(View):
    
    def get(self, request, *args, **kwargs):
        item_list = Item.objects.all()
        context = {
                'item_list': item_list,
        }
        return render(request, 'item_list.html', context=context)


class Product(View):
    
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, id=kwargs['id'])
        context = {'item': item}
        return render(request, 'show.html', context=context)
