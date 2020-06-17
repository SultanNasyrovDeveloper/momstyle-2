from session_object.service import SessionObjectService


def favorites_items_number(request):
    service = SessionObjectService('favorites')
    favorites = service.get_or_create(request)
    return {
        'favorites_items_number': favorites.get_items_number(),
        'favorites': [item.product_id for item in favorites.items]
    }
