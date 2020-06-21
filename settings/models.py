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

    phone_number = models.CharField(max_length=150, verbose_name='Номер телефона', null=True, blank=True)
    email = models.EmailField(null=True, blank=True, verbose_name='Электронный адрес')
    address = models.CharField(max_length=500, null=True, blank=True, verbose_name='Адрес (через запятую)')
    working_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name='Часы работы')
    delivery_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы доставка',
                                              null=True, blank=True)
    about_header_image = models.ImageField(upload_to='header_images/', verbose_name='Изображение страницы о нас',
                                           null=True, blank=True)

    organisation_line1 = models.CharField(max_length=150, default='', blank=True, verbose_name='Организация(строка 1)')
    organisation_line2 = models.CharField(max_length=150, default='', blank=True, verbose_name='Организация(строка 2)')
    organisation_line3 = models.CharField(max_length=150, default='', blank=True, verbose_name='Организация(строка 3)')
    organisation_line4 = models.CharField(max_length=150, default='', blank=True, verbose_name='Организация(строка 4)')

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки'

    def addresses(self):
        if self.address:
            return self.address.split(', ')

    def phone_numbers(self):
        if self.phone_number:
            return self.phone_number.split(', ')


class SocialLink(models.Model):
    name = models.CharField(max_length=50,)
    active = models.BooleanField(default=False, verbose_name='Доступна')
    show_in_navbar = models.BooleanField(default=False, verbose_name='Отображается в шапке')
    link = models.CharField(
        max_length=250, verbose_name='Ссылка или номер', default='', null=True, blank=True,
    )

    class Meta:
        verbose_name = 'Ссылки на соц сети'
        verbose_name_plural = 'Ссылки на соц сети'

    def __str__(self):
        return self.name




