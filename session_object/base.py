from shop.models import Product


class BaseSessionObjectItem:
    def __init__(self, **kwargs):
        self.product_id = kwargs.get('product_id')

    @property
    def product(self):
        return Product.objects.get(id=int(self.product_id))


class BaseSessionObject:
    def __init__(self, items=None):
        self.items = items or []

    def __contains__(self, product_id):
        if self._get_item_by_product_id(product_id):
            return True
        return False

    def get_items_number(self):
        return len(self.items)

    def clean(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def remove_item_by_product_id(self, product_id):
        if product_id in self:
            item = self._get_item_by_product_id(product_id)
            self.remove_item(item)

    def _get_item_by_product_id(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                return item