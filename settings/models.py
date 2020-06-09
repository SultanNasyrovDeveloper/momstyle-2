from django.db import models


class DeliveryPaymentInfo(models.Model):
    types = (
        ('d', 'Информация о доставке'),
        ('p', 'Информация об оплате')
    )
    type = models.CharField(max_length=20, choices=types, null=True, blank=True, verbose_name='Тип')
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    image = models.FileField(upload_to='delivery/', verbose_name='Иконка', help_text='В формате svg', blank=True, null=True)
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Информация о доставке и оплате'
        verbose_name_plural = 'Информация о доставке и оплате'

    def __str__(self):
        return self.title


class Banner(models.Model):
    """Contains images for banner app on index page of the site"""

    image = models.ImageField(upload_to='banner/', verbose_name='Изображение, размер ~ 300 КБ')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        ordering = ['position']

    def __str__(self):
        return 'Баннер {}'.format(self.position)


class SiteMain(models.Model):

    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип', null=True, blank=True)
    sizes_table = models.ImageField(upload_to='sizes/', null=True, blank=True, verbose_name='Таблица размеров')

    category_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока категории')
    category_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока категории')
    product_h2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название блока продукты')
    product_par = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описание блока продукты')

    vk_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу вк')
    insta_url = models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу инстаграм')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Электронный адрес')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес')
    working_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name='Часы работы')
    delivery_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы доставка',
                                              null=True, blank=True)
    about_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы о нас',
                                           null=True, blank=True)

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки'





