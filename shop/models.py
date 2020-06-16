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
    available = models.BooleanField(default=True, verbose_name='Доступен')

    name = models.CharField(max_length=300, default='', blank=True, null=True, verbose_name='Название')
    category = models.ManyToManyField(ProductCategory, verbose_name='Категории')
    sizes = models.ManyToManyField(
        ProductSize, related_name='sizes', related_query_name='sizes', verbose_name='Размеры',
    )

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

    def get_default_size(self):
        return self.size


class ProductImage(models.Model):
    """"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', related_query_name='images')
    file = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ('id', )

    def __str__(self):
        return 'Изображение товара ' + str(self.id)