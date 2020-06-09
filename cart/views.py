from django.shortcuts import render, Http404, HttpResponse
from django.core.mail import send_mail
from seo.models import SitePageSeo
from momstyle_2 import settings
from .cart import Cart

from django.views.decorators.csrf import csrf_exempt

import json


def cart(request):
    cart = Cart(request)
    seo, _ = SitePageSeo.objects.get_or_create(page_name='Корзина')
    context = {
        'cart_items': cart.get_items_list(),
        'total': cart.total(),
        'page_seo': seo
    }
    return render(request, 'cart.html', context)


@csrf_exempt
def add_item(request):

    if request.method =='POST' and request.is_ajax():
        cart = Cart(request)
        product_id, size, quantity = request.POST['product_id'], request.POST['size'], request.POST['quantity']
        cart.add_item(product_id, size, quantity)
        response = {'items': cart.count_items()}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


@csrf_exempt
def delete_item(request):

    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        key = request.POST['key']
        cart.delete_item(key)
        response = {
            'items': cart.count_items(),
            'total': cart.total()
        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


@csrf_exempt
def change_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        key, quantity = request.POST['key'], request.POST['quantity']
        cart.change_quantity(key, quantity)
        response = {'total': cart.total(), 'subtotal': cart.cart[key]['subtotal']}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


@csrf_exempt
def clean(request):
    if request.method == 'GET' and request.is_ajax():
        cart = Cart(request)
        cart.clean()
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


@csrf_exempt
def make_order(request):

    if request.method == 'POST' and request.is_ajax():
        name, phone = request.POST['name'], request.POST['phone_number']
        cart = Cart(request)
        order = cart.make_order(name, phone)
        msg = '[{}]: С сайта поступил новый заказ № {} на сумму {} руб'.format(order.date, order.id, order.total)
        send_mail('Поступил новый заказ', msg,
                  settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=True)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


