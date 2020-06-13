from django.db import models


class AboutUsBlock(models.Model):
    title = models.CharField('Заголовок блока', max_length=1000, )
    text = models.TextField('Текст блока', default='', blank=True)

    class Meta:
        verbose_name = 'Блок о нас'
        verbose_name_plural = 'Блоки о нас'

    def __str__(self):
        return self.title


class AboutUsBlockImage(models.Model):
    block = models.ForeignKey(
        AboutUsBlock, on_delete=models.CASCADE, related_name='images', verbose_name='Блок',
    )
    file = models.ImageField('Изображение', upload_to='about_us_images/', )

    class Meta:
        verbose_name = 'Изображение блока'
        verbose_name_plural = 'Изображения блока'

    def __str__(self):
        return f'Изображение № {self.id} блока {self.block.title}'