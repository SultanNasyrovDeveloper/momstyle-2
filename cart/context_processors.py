from .cart import Cart


def cart(request):
    cart = Cart(request)
    return {'cart_items_number': cart.count_items()}
