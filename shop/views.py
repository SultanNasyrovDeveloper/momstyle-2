from django.shortcuts import render, Http404, HttpResponse, get_object_or_404
from django.views import generic

from settings.models import Banner, DeliveryPaymentInfo
from seo.models import SitePageSeo

from .models import ProductCategory, Product, ContactPerson

import json
import random


def random_queryset(class_name, number, except_id=None):
    """ Returns queryset of random [number] items of given class """
    ids = list(class_name.displayed.values_list('id', flat=True))
    if except_id:
        ids.remove(int(except_id))
    try:
        random_ids = random.sample(ids, number)
    except ValueError:
        random_ids = []
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
            'page_seo': seo
        }
        return render(request, 'index.html', context)


class Catalog(generic.View):

    page_name = 'Каталог'

    def get(self, request, category):
        context = {}
        if category == 'all':
            products = Product.displayed.all()
        else:
            category = ProductCategory.objects.get(id=int(category))
            products = Product.displayed.filter(category=category)
        context['products'] = products
        context['categories'] = ProductCategory.objects.all()
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context['page_seo'] = seo
        return render(request, 'catalog.html', context)


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
        return context


def contact_us(request):
    if request.method == 'POST' and request.is_ajax():
        name, phone = request.POST['name'], request.POST['phone']
        ContactPerson.objects.create(name=name, phone=phone)
        return HttpResponse({})
    else:
        raise Http404

