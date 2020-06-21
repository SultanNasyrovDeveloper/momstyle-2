from django.db import models


class DeliveryMethod(models.Model):

    name = models.CharField('Название', max_length=1000)
    price = models.PositiveIntegerField('Стоимость (руб.)', default=0)

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

    def __str__(self):
        price = f'{self.price} руб.' if self.price else "Бесплатно"
        return f'{self.name} ({price})'


class DeliveryPartners(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    logo = models.FileField(upload_to='delivery_partners', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Партнер доставки'
        verbose_name_plural = 'Партнеры доставки'

    def __str__(self):
        return self.name
