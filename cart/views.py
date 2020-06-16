import json

from django.views import generic
from django.shortcuts import render, Http404, HttpResponse, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import JsonResponse

from seo.models import SitePageSeo
from session_object.service import SessionObjectService
from order.forms import QuickBuyForm

from .serializers import CartItemSerializer


class CartView(generic.View):
    def get(self, request, *args, **kwargs):
        seo, _ = SitePageSeo.objects.get_or_create(page_name='Корзина')
        service = SessionObjectService('cart')
        cart = service.get_or_create(request)
        context = {
            'page_seo': seo,
            'cart': service.serialize(cart),
            'quick_buy_form': QuickBuyForm()
        }
        return render(request, 'cart.html', context)

    def post(self, request, *args, **kwargs):
        form = QuickBuyForm(request.POST)
        if form.is_valid():
            order = form.save()
            service = SessionObjectService('cart')
            session_cart = service.get_or_create(request)
            order.parse_session_cart(session_cart)
            return redirect(reverse_lazy('order:complete'))
        else:
            return redirect('cart')


def add_item(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        service = SessionObjectService('cart')
        cart = service.get_or_create(request)
        serializer = CartItemSerializer(data=post_data)
        if serializer.is_valid():
            item = serializer.save()
            if item in cart:
                response = {
                    'text': 'Данный товар уже в корзине.',
                    'items_number': cart.get_items_number(),
                    'total_price': cart.get_total_price(),
                }
                return JsonResponse(response)
            cart.add_item(item)
            service.save(request, session_object=cart)
            response = {
                'text': 'Товар добавлен в корзину.',
                'items_number': cart.get_items_number(),
                'total_price': cart.get_total_price(),
            }
            return JsonResponse(response)
        else:
            raise Http404
    else:
        raise Http404()


def remove_item(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        service = SessionObjectService('cart')
        cart = service.get_or_create(request)
        cart.remove_item_by_product_id_and_size(
            post_data.get('id'), post_data.get('size'),
        )
        service.save(request, cart)
        return JsonResponse({
            'text': 'Товар удален из корзины.',
            'items_number': cart.get_items_number(),
            'total_price': cart.get_total_price(),
        })
    else:
        raise Http404()


def change_item_quantity(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        service = SessionObjectService('cart')
        cart = service.get_or_create(request)
        changed_item = cart.change_item_quantity(
            post_data.get('id'), post_data.get('size'), int(post_data.get('quantity')),
        )
        service.save(request, cart)
        context = {
            'text': 'Количество изменено.',
            'item_total': changed_item.get_total_price(),
            'cart_total': cart.get_total_price(),
        }
        return JsonResponse(context)
    else:
        raise Http404()

