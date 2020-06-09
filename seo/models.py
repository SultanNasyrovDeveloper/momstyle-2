from django.db import models
from django.db.models.signals import post_save

from shop.models import Product


class PageSeo(models.Model):

    title = models.CharField(max_length=750, null=True, blank=True, verbose_name='Title',
                             help_text='Данный текст будет идти после названия продукта: Например, Юбка - текст title')
    description = models.CharField(
        max_length=1000, null=True, blank=True, verbose_name='Description',
        help_text='Данный текст будет идти после названия продукта: Например, Юбка - текст description')
    keywords = models.CharField(max_length=750, null=True, blank=True, verbose_name='Keywords')

    additional_html = models.TextField(verbose_name='Дополнительное', null=True, blank=True,
                                       help_text='Дополнительные теги будут в блоке head на странике товара')

    class Meta:
        verbose_name = 'Seo страницы'
        verbose_name_plural = 'Seo страниц сайта'
        abstract = True


class SitePageSeo(PageSeo):
    page_name = models.CharField(max_length=250, verbose_name='Название страницы')

    def __str__(self):
        return 'Seo для страницы сайта {}'.format(self.page_name)


class ProductPageSeo(PageSeo):
    product = models.OneToOneField(
        'shop.Product', on_delete=models.CASCADE, related_name='page_seo', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Seo страницы товара'
        verbose_name_plural = 'Seo страниц товаров'

    def __str__(self):
        return 'Seo для страницы товара {}'.format(self.product.name)


def create_checklist(sender, **kwargs):
    if kwargs.get('created', None):
        ProductPageSeo.objects.create(product=kwargs.get('instance'))


post_save.connect(create_checklist, sender=Product)


