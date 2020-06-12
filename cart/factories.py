


def simple_cart_factory(request):
    if not 'cart' in request.session:
        request.session['cart'] = {}

    return