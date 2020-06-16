import random

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from settings.models import Banner, DeliveryPaymentInfo
from seo.models import SitePageSeo
from order.forms import QuickBuyForm
from order.models import OrderItem

from .models import ProductCategory, Product
from . import filters


def random_queryset(class_name, number, except_id=None):
    """ Returns queryset of random [number] items of given class """
    ids = list(class_name.displayed.values_list('id', flat=True))
    if except_id:
        ids.remove(int(except_id))
    try:
        random_ids = random.sample(ids, number)
    except ValueError:
        random_ids = ids
    queryset = class_name.displayed.filter(id__in=random_ids)
    return queryset


class Index(generic.View):

    page_name = 'Главная страница'

    def get(self, request):
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context = {
            'banners': Banner.objects.all(),
            'categories': ProductCategory.objects.all(),
            'products': Product.displayed.all()[:6],
            'page_seo': seo,
        }
        return render(request, 'index.html', context)


class ProductListView(generic.View):

    page_name = 'Каталог'

    def get(self, request, *args, **kwargs):
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context = {
            'filter': filters.ProductFilter(request.GET, queryset=Product.displayed.all()),
            'page_seo': seo,
        }
        return render(request, 'product_list.html', context)


class ProductQuickBuyView(generic.View):

    def post(self, request, *args, **kwargs):
        form = QuickBuyForm(request.POST)
        product = Product.objects.get(id=kwargs.get('pk'))

        if form.is_valid():
            order = form.save()
            OrderItem.objects.create(
                order=order, product_id=product.id, product_name=product.name,
            )
            return redirect(reverse_lazy('order:complete'))
        else:
            return redirect(product.get_absolute_url())


class Delivery(generic.View):
    page_name = 'Информация об оплате и доставке'

    def get(self, request):
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context = {
            'info': DeliveryPaymentInfo.objects.all(),
            'page_seo': seo
        }
        return render(request, 'delivery.html', context)


class ProductDetailView(generic.DetailView):
    queryset = Product.displayed.all()
    template_name = 'product_detail.html'
    context_object_name = 'target'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suggestions'] = random_queryset(Product, 6, self.kwargs.get('pk'))
        context['page_seo'] = self.object.page_seo
        context['quick_buy_form'] = QuickBuyForm()
        return context

