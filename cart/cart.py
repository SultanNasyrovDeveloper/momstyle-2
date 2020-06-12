from shop.models import Product, Order, OrderItem


class CartItem:
    def __init__(self, product_id, quantity=1, size=None):
        self.product_id = product_id
        self.quantity = quantity
        self.size = size or self.product.get_default_size()

    @property
    def product(self):
        return Product.objects.get(id=int(self.product_id))

    def get_total_price(self):
        return self.product.price * self.quantity


class Cart:
    def __init__(self):
        self.items = []

    def get_items_number(self):
        return len(self.items)

    def get_total_price(self):
        return sum([item.get_total_price() for item in self.items])

    def clean(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def change_item_quantity(self, item_product_id, new_quantity):
        item = self._get_item_by_product_id(item_product_id)
        item.quantity = new_quantity

    def change_item_size(selfself, itm_product_id, new_size):
        pass

    def _get_item_by_product_id(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                return item
