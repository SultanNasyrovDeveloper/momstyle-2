from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save


class ProductsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(display=True)


class ProductCategory(models.Model):
    """Product category"""
    name = models.CharField(max_length=300, default='', verbose_name='Категория товаров')
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    """"""
    name = models.CharField(max_length=300, default='', verbose_name='Размер')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Product(models.Model):
    """"""
    display = models.BooleanField(default=True, verbose_name='Отображается')

    name = models.CharField(max_length=300, default='', blank=True, null=True, verbose_name='Название')
    category = models.ManyToManyField(ProductCategory, verbose_name='Категории')
    size = models.ManyToManyField(ProductSize, related_name='sizes', related_query_name='sizes', verbose_name='Размеры')

    prev_price = models.PositiveIntegerField(default=None, null=True, blank=True, verbose_name='Цена без скидки')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')

    material = models.CharField(max_length=200, default='', null=True, blank=True, verbose_name='Состав')
    models_height = models.PositiveSmallIntegerField(default=165, verbose_name='Рост модели')
    description = models.TextField(default='', verbose_name='Описание товара')

    objects = models.Manager()
    displayed = ProductsManager()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})


class ProductImage(models.Model):
    """"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', related_query_name='images')
    image_full = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение')
    image_mini = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение(миниатюра)')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('id', )

    def __str__(self):
        return 'Изображение товара ' + str(self.id)


class Order(models.Model):
    processed = models.BooleanField(default=False, verbose_name='Обработан')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    customer = models.CharField(max_length=200, default='', verbose_name='Покупатель')
    phone_number = models.CharField(max_length=20, default='', verbose_name='Номер телефона')
    total = models.PositiveIntegerField(default=0, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']

    def __str__(self):
        return 'Заказ {}'.format(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    name = models.CharField(max_length=300, default='', verbose_name='Название')
    size = models.CharField(max_length=50, default='', verbose_name='Размер')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    subtotal = models.PositiveIntegerField(default=0, verbose_name='Сумма')


class ContactPerson(models.Model):
    processed = models.BooleanField(default=False, verbose_name='Перезвонили')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Номер Телефона')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заявки')

    class Meta:
        verbose_name = 'Заявка связаться с нами'
        verbose_name_plural = 'Заявки связаться с нами'
        ordering = ['-date']

    def __str__(self):
        return self.name
