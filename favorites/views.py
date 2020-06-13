import json

from django.shortcuts import render, Http404
from django.http import JsonResponse

from session_object.service import SessionObjectService

from .favorites import FavoritesItem


def add_item(request):
    if request.method == 'POST':
        post_data = json.loads(request.body)
        service = SessionObjectService('favorites')
        favorites = service.get_or_create(request)
        item = FavoritesItem(product_id=post_data.get('id'))
        response = {
            'text': 'Данный товар уже находится в избранном.'
        }
        if item.product_id not in favorites:
            favorites.add_item(item)
            service.save(request, favorites)
            response['text'] = 'Товар добавлен в избранное.'
        favorites = request.session['favorites']
        return JsonResponse(response)
    else:
        raise Http404('Only post allowed')
