

class OrderIncompleteMessage:
    def __init__(self, cart, order):
        self.cart = cart
        self.order = order

    def render(self) -> str:
        return 'Форма заказа не заполнена'