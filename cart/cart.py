from session_object.base import BaseSessionObject, BaseSessionObjectItem


class CartItem(BaseSessionObjectItem):
    def __init__(self, product_id, size, quantity=1):
        super().__init__(product_id=product_id)
        self.quantity = quantity
        self.size = size

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart(BaseSessionObject):

    def __contains__(self, item):
        if self._get_item_by_product_id(item.product_id):
            item_with_same_id = self._get_item_by_product_id(item.product_id)
            if item_with_same_id.size == item.size:
                return True
        return False

    def get_total_price(self):
        return sum([item.get_total_price() for item in self.items])

    def change_item_quantity(self, item_product_id, size, new_quantity):
        item = self.get_item_by_id_and_size(item_product_id, size)
        item.quantity = new_quantity
        return item

    def add_item(self, item):
        if item not in self:
            self.items.append(item)

    def remove_item_by_product_id_and_size(self, product_id, size):
        item = self.get_item_by_id_and_size(product_id, size)
        if item:
            self.items.remove(item)

    def get_item_by_id_and_size(self, product_id, size):
        for item in self.items:
            if item.product_id == product_id and item.size == size:
                return item

