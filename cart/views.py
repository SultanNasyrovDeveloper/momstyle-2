import json

from django.views import generic
from django.shortcuts import render, Http404, HttpResponse
from django.core.mail import send_mail
from django.http import JsonResponse

from seo.models import SitePageSeo

# from .services import CartService


class CartView(generic.View):
    def get(self, request, *args, **kwargs):
        seo, _ = SitePageSeo.objects.get_or_create(page_name='Корзина')
        # cart = CartService.get_or_create(request)
        context = {
            'page_seo': seo,
            'cart': CartService.serialize_cart(cart)
        }
        return render(request, 'cart.html', context)

#
# def cart(request):
#     cart = Cart(request)
#
#     context = {
#         'cart_items': cart.get_items_list(),
#         'total': cart.total(),
#         'page_seo': seo
#     }
#     return render(request, , context)
#
# def test(request):
#
#     return HttpResponse({'status': 20})
#
#
# @csrf_exempt
# def delete_item(request):
#
#     # if request.method == 'POST' and request.is_ajax():
#     #     cart = Cart(request)
#     #     key = request.POST['key']
#     #     cart.delete_item(key)
#     #     response = {
#     #         'items': cart.count_items(),
#     #         'total': cart.total()
#     #     }
#     #     return HttpResponse(json.dumps(response))
#     # else:
#         raise Http404
#
#
# @csrf_exempt
# def change_quantity(request):
#     # if request.method == 'POST' and request.is_ajax():
#     #     cart = Cart(request)
#     #     key, quantity = request.POST['key'], request.POST['quantity']
#     #     cart.change_quantity(key, quantity)
#     #     response = {'total': cart.total(), 'subtotal': cart.cart[key]['subtotal']}
#     #     return HttpResponse(json.dumps(response))
#     # else:
#         raise Http404
#
#
# @csrf_exempt
# def clean(request):
#     # if request.method == 'GET' and request.is_ajax():
#     #     cart = Cart(request)
#     #     cart.clean()
#     #     response = {}
#     #     return HttpResponse(json.dumps(response))
#     # else:
#         raise Http404
#
#
# @csrf_exempt
# def make_order(request):
#
#     # if request.method == 'POST' and request.is_ajax():
#     #     name, phone = request.POST['name'], request.POST['phone_number']
#     #     cart = Cart(request)
#     #     order = cart.make_order(name, phone)
#     #     msg = '[{}]: С сайта поступил новый заказ № {} на сумму {} руб'.format(order.date, order.id, order.total)
#     #     send_mail('Поступил новый заказ', msg,
#     #               settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], fail_silently=True)
#     #     response = {}
#     #     return HttpResponse(json.dumps(response))
#     # else:
#         raise Http404
#
#
