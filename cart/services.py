from typing import Dict

from .cart import Cart
from .serializers import CartSerializer


class CartService:
    @classmethod
    def get_or_create(cls, request) -> Cart:
        """
        Retrieve cart cart from the session if exists else create new.
        """
        if 'cart' not in request.session:
            request.session['cart'] = {}
        return cls.deserialize_cart(request.session['cart'])

    @classmethod
    def save_cart(cls, request, cart) -> None:
        """
        Save cart to the session.
        """
        serialized_cart = cls.serialize_cart(cart)
        request.session['cart'] = serialized_cart

    @classmethod
    def serialize_cart(cls, cart) -> Dict:
        """
        Serialize cart instance.
        """
        return CartSerializer(cart)

    @classmethod
    def deserialize_cart(cls, cart_data):
        return CartSerializer(data=cart_data).instance
