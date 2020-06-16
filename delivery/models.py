from django.db import models


class DeliveryMethod(models.Model):

    name = models.CharField('Название', max_length=1000)
    price = models.PositiveIntegerField('Стоимость (руб.)', default=0)

    class Meta:
        verbose_name = 'Способ доставки'
        verbose_name_plural = 'Способы доставки'

    def __str__(self):
        return f'{self.name} ({self.price or "Бесплатно"})'


