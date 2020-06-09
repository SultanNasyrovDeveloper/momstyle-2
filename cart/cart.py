from shop.models import Product, Order, OrderItem


class CartItem(object):
    """Cart Item """
    def __init__(self, product_id, size, quantity):
        product = Product.objects.get(id=product_id)
        subtotal = product.price * int(quantity)
        self.key = product.name + ' ({})'.format(size)
        self.name = product.name
        self.quantity = int(quantity)
        self.size = str(size)
        self.price = int(product.price)
        self.id = product.id
        self.subtotal = subtotal

    def to_dict(self):
        cart_item_dict = {
            'id': self.id,
            'name': self.name,
            'quantity': self.quantity,
            'size': self.size,
            'price': self.price,
            'subtotal': self.subtotal,
        }
        return cart_item_dict


class Cart(object):
    """"""
    def __init__(self, request):

        self.session = request.session

        if 'cart' in self.session:
            self.cart = self.session['cart']
        else:
            self.cart = {}

    def save(self):
        self.session['cart'] = self.cart

    def count_items(self):
        return len(self.cart)

    def get_items_list(self):
        return list(self.cart.values())

    def add_item(self, product_id, size, quantity):

        item = CartItem(product_id, size, quantity)

        if item.key in self.cart:
            if self.cart[item.key]['size'] == item.size:
                self.cart[item.key]['quantity'] = item.quantity
                self.cart[item.key]['subtotal'] = item.subtotal
                self.save()
        else:
            self.cart[item.key] = item.to_dict()
            self.save()

    def change_quantity(self, key, new_quantity):
        self.cart[key]['quantity'] = int(new_quantity)
        self.cart[key]['subtotal'] = int(self.cart[key]['price']) * int(new_quantity)
        self.save()

    def delete_item(self, key):
        self.cart.pop(key)
        self.save()

    def clean(self):
        self.cart = {}
        self.save()

    def total(self):
        total = 0
        for item in self.get_items_list():
            total += int(item['subtotal'])
        return total

    def make_order(self, name, phone_number):
        order = Order(customer=name, phone_number=phone_number, total=self.total())
        order.save()
        for item in self.get_items_list():
            order_item = OrderItem(order=order, name=item['name'], size=item['size'],
                                   price=item['price'], quantity=item['quantity'], subtotal=item['subtotal'])
            order_item.save()
        self.clean()
        return order
