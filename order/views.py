from django.shortcuts import render, redirect, Http404, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from utils import notify_admin
from seo.models import SitePageSeo
from session_object.service import SessionObjectService
from payment.models import PaymentMethod
from delivery.models import DeliveryMethod

from . import forms, models
from .utils import get_payment_url
from .order_incomplete_message import OrderIncompleteMessage


def redirect_to_form(request):
    service = SessionObjectService('order')
    order_data = service.get_or_create(request)
    if 'current_form' in order_data:
        return redirect(reverse_lazy('order:' + order_data['current_form']))
    else:
        return redirect(reverse_lazy('order:personal_info'))


class OrderPersonalInfoCheckoutView(generic.View):
    page_name = 'Оформление заказа: форма персональных данных'

    def get_context_data(self, request):
        service = SessionObjectService('order')
        cart_service = SessionObjectService('cart')
        cart = cart_service.get_or_create(request)
        order_data = service.get_or_create(request)
        initial = {
            'first_name': order_data.get('first_name', None),
            'second_name': order_data.get('second_name', None),
            'email': order_data.get('email', None),
            'phone_number': order_data.get('phone_number', None),
        }
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        form = forms.OrderPersonalInformationForm(initial=initial, )
        context = {
            'seo': seo,
            'form': form,
            'order': order_data,
            'cart': cart_service.serialize(cart)
        }
        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(request)

        return render(request, 'checkout_personal_info.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.OrderPersonalInformationForm(data=request.POST)
        if form.is_valid():
            service = SessionObjectService('order')
            order = service.get_or_create(request)
            order.update(form.cleaned_data)
            order['current_form'] = 'delivery'
            service.save(request, order)
            return redirect(reverse_lazy('order:delivery'))
        else:
            context = self.get_context_data(request)
            context['form'] = form
            return render(request, 'checkout_personal_info.html', context)


class OrderDeliveryCheckoutView(generic.View):
    page_name = 'Оформление заказа: способ доставки'

    def get_context_data(self, request):
        service = SessionObjectService('order')
        order_data = service.get_or_create(request)
        cart_service = SessionObjectService('cart')
        cart = cart_service.get_or_create(request)
        initial = {
            'delivery_method': order_data.get('delivery_method', None),
            'index': order_data.get('index', None),
            'city': order_data.get('city', None),
            'street': order_data.get('street', None),
            'building_number': order_data.get('building_number', None),
            'apartment': order_data.get('apartment', None),
            'order': order_data,
        }
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        form = forms.OrderDeliveryForm(initial=initial)
        context = {
            'seo': seo,
            'form': form,
            'cart': cart_service.serialize(cart)
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, 'checkout_delivery.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.OrderDeliveryForm(data=request.POST)
        if form.is_valid():
            service = SessionObjectService('order')
            order = service.get_or_create(request)
            order.update(form.cleaned_data)
            service.save(request, order)
            order['current_form'] = 'payment'
            return redirect(reverse_lazy('order:payment'))
        else:
            context = self.get_context_data(request)
            context['form'] = form
            return render(request, 'checkout_delivery.html', context)


class OrderPaymentCheckoutView(generic.View):
    page_name = 'Оформление заказа: способ оплаты'

    def get_context_data(self, request):
        service = SessionObjectService('order')
        cart_service = SessionObjectService('cart')
        cart = cart_service.get_or_create(request)
        order_data = service.get_or_create(request)
        initial = {
            'payment_method': order_data.get('payment_method', None),

        }
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        form = forms.OrderPaymentMethodForm(initial=initial)
        delivery_method = DeliveryMethod.objects.get(id=order_data.get('delivery_method'))
        context = {
            'seo': seo,
            'form': form,
            'order': order_data,
            'delivery_method': delivery_method,
            'order_total_price': cart.get_total_price() + delivery_method.price,
            'cart': cart_service.serialize(cart)

        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request)
        return render(request, 'checkout_payment.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.OrderPaymentMethodForm(data=request.POST)
        if form.is_valid():
            service = SessionObjectService('order')
            order = service.get_or_create(request)
            order.update(form.cleaned_data)
            service.save(request, order)
            order['current_form'] = 'checkout'
            return redirect(reverse_lazy('order:checkout'))
        else:
            context = self.get_context_data(request)
            context['form'] = form
            return render(request, 'checkout_payment.html', context)


class OrderCheckoutView(generic.View):
    page_name = 'Оформление заказа: способ оплаты'

    def get_context_data(self, request):
        order_service = SessionObjectService('order')
        cart_service = SessionObjectService('cart')
        cart = cart_service.get_or_create(request)
        order = order_service.get_or_create(request)
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        delivery_method = DeliveryMethod.objects.get(id=order.get('delivery_method'))
        form = forms.OrderForm()
        context = {
            'seo': seo,
            'form': form,
            'order': order,
            'payment_method': PaymentMethod.objects.get(id=order.get('payment_method')),
            'delivery_method': delivery_method,
            'order_total_price': cart.get_total_price() + delivery_method.price,
            'cart': cart_service.serialize(cart)
        }
        return context

    def get(self, request, *args, **kwargs):
        try:
            context = self.get_context_data(request)
        except Exception:
            redirect(reverse_lazy('order:personal-info'))
        return render(request, 'checkout.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.OrderForm(data=request.POST)
        if form.is_valid():
            created_order = form.save()
            cart_service = SessionObjectService('cart')
            order_service = SessionObjectService('order')
            created_order.parse_session_cart(cart_service.get_or_create(request))
            created_order.parse_session_order(order_service.get_or_create(request))
            cart_service.new(request)
            if created_order.payment.payment_method_id == 1:
                return redirect(get_payment_url(created_order.id, created_order.get_total_price()))
            return redirect(reverse_lazy('order:complete'))
        else:
            context = self.get_context_data(request)
            context['form'] = form
            return render(request, 'checkout.html', context)


class CheckoutCompleteView(generic.DetailView):
    queryset = models.Order.objects.all()
    template_name = 'checkout_complete.html'
    context_object_name = 'order'


def order_incomplete(request):
    if request.method == 'POST':
        cart_service = SessionObjectService('cart')
        order_service = SessionObjectService('order')
        cart = cart_service.get_or_create(request)
        order = order_service.get_or_create(request)
        message = OrderIncompleteMessage(cart, order)
        notify_admin(
            'Незаполненная форма заказа.',
            message.render()
        )
        return HttpResponse({})
    else:
        raise Http404('Order incomplete')
