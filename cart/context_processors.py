from session_object.service import SessionObjectService


def cart_items_number(request):
    service = SessionObjectService('cart')
    cart = service.get_or_create(request)
    return {'cart_items_number': cart.get_items_number()}
