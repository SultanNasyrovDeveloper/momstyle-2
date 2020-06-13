from session_object.base import BaseSessionObject, BaseSessionObjectItem


class CartItem(BaseSessionObject):
    def __init__(self, product_id, size, quantity=1):
        super().__init__(product_id=product_id)
        self.quantity = quantity
        self.size = size

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(BaseSessionObjectItem):

    def get_total_price(self):
        return sum([item.get_total_price() for item in self.items])

    def change_item_quantity(self, item_product_id, new_quantity):
        item = self._get_item_by_product_id(item_product_id)
        item.quantity = new_quantity

    def change_item_size(selfself, itm_product_id, new_size):
        pass
