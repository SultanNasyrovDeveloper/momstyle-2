from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class OrderItem(models.Model):
    order = models.ForeignKey(
        'order.Order', on_delete=models.CASCADE, related_name='items', verbose_name='Заказ',
        default=None, null=True,
    )
    product_id = models.PositiveIntegerField(default=1)
    product_name = models.CharField(max_length=1000, verbose_name='Название продукта')
    size = models.CharField(max_length=50, verbose_name='Размер')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')

    @property
    def total_price(self):
        return self.get_total_price()

    def get_total_price(self):
        return self.price * self.quantity


class Order(models.Model):

    fast_buy = models.BooleanField('В 1 клик', default=False,)

    no_connect = models.BooleanField('Без обратной связи', default=False, blank=True,)
    connect_by_phone = models.BooleanField('Связаться по телефону', default=False, blank=True)
    connect_by_whatsapp = models.BooleanField('Связаться по whatsapp', default=False, blank=True)
    comment = models.TextField('Комментарий покупателя', default='', blank=True)

    created = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} от {self.created}'

    @property
    def total_price(self):
        return self.get_total_price()

    def parse_session_cart(self, session_cart):
        for item in session_cart.items:
            OrderItem.objects.create(
                order=self, product_id=item.product_id, product_name=item.product.name,
                size=item.size, price=item.product.price, quantity=item.quantity,
            )

    def parse_session_order(self, session_order):
        personal_information = self.personal_info
        personal_information.first_name = session_order.get('first_name')
        personal_information.second_name = session_order.get('second_name')
        personal_information.phone_number = session_order.get('phone_number')
        personal_information.email = session_order.get('email')
        personal_information.save()

        delivery_info = self.delivery
        delivery_info.delivery_method_id = session_order.get('delivery_method')
        delivery_info.index = session_order.get('index')
        delivery_info.city = session_order.get('city')
        delivery_info.street = session_order.get('street')
        delivery_info.building_number = session_order.get('building_number')
        delivery_info.apartment = session_order.get('apartment')
        delivery_info.save()

        payment_info = self.payment
        payment_info.payment_method_id = session_order.get('payment_method')
        payment_info.save()

    def get_total_price(self):
        return sum([
            item.get_total_price() for item in self.items.all()
        ]) + self.delivery.delivery_method.price


class OrderPersonalInformation(models.Model):
    order = models.OneToOneField(
        'order.Order',
        on_delete=models.CASCADE,
        related_name='personal_info',
        verbose_name='Заказ',
    )
    first_name = models.CharField('Имя', max_length=250, default='')
    second_name = models.CharField('Фамилия', max_length=250, default='')
    email = models.EmailField('Электронная почта', max_length=250, default='')
    phone_number = models.CharField('Номер телефона', max_length=250, default='')


class OrderDeliveryInformation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='delivery')
    delivery_method = models.ForeignKey(
        'delivery.DeliveryMethod', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Метод доставки',
    )
    price = models.IntegerField('Стоимость', default=0)
    index = models.CharField(max_length=10, verbose_name='Индекс', default='')
    city = models.CharField(max_length=500, verbose_name='Населенный пункт (город)', default='')
    street = models.CharField(max_length=500, verbose_name='Улица', default='')
    building_number = models.CharField(max_length=20, verbose_name='Номер дома', default='')
    apartment = models.CharField(max_length=20, verbose_name='Квартира', default='')


class OrderPaymentInformation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.ForeignKey(
        'payment.PaymentMethod', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Метод оплаты',
    )


@receiver(post_save, sender=Order)
def create_payment_and_delivery(sender, created,  **kwargs):
    if created:
        order = kwargs.get('instance')
        OrderPersonalInformation.objects.create(order=order)
        OrderDeliveryInformation.objects.create(order=order)
        OrderPaymentInformation.objects.create(order=order)
