import json

from django.shortcuts import render, Http404
from django.http import JsonResponse
from django.views import generic

from session_object.service import SessionObjectService

from seo.models import SitePageSeo
from shop.models import Product
from shop.filters import ProductFilter

from .favorites import FavoritesItem


class FavoritesView(generic.View):

    page_name = 'Избранное'

    def get(self, request, *args, **kwargs):
        service = SessionObjectService('favorites')
        favorites = service.get_or_create(request)
        seo, _ = SitePageSeo.objects.get_or_create(page_name=self.page_name)
        context = {
            'seo': seo,
            'filter': ProductFilter(request.GET, queryset=Product.displayed.filter(
                id__in=[item.product_id for item in favorites.items]
            )),
            'is_favorites': True
        }
        return render(request, 'product_list.html', context)


def toggle_item(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        service = SessionObjectService('favorites')
        favorites = service.get_or_create(request)
        product_id = int(post_data.get('id'))
        if product_id in favorites:
            item = favorites._get_item_by_product_id(product_id)
            favorites.remove_item(item)
            service.save(request, favorites)
            response = {
                'text': 'Товар удален из избранного',
                'status': 201
            }
        else:
            item = FavoritesItem(product_id=post_data.get('id'))
            favorites.add_item(item)
            service.save(request, favorites)
            response = {
                'text': 'Товар добавлен в избранное',
                'status': 200
            }
        return JsonResponse(response)
    else:
        raise Http404('Only post allowed')
