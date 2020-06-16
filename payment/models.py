from django.db import models
from django.db.models.signals import post_save


class PaymentMethod(models.Model):
    name = models.CharField('Название', max_length=1000)

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

    def __str__(self):
        return self.name

    def delete(self, **kwargs):
        if self.id == 1:
            raise Exception('Невозможно удалить оплату онлайн.')
        return super().delete(**kwargs)
