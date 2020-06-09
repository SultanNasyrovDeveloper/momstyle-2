from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    """"""
    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Название поста')
    image = models.ImageField(upload_to='blog/', verbose_name='Главное изображение поста')
    likes_number = models.IntegerField(default=0, verbose_name='Количество лайков',
                                       help_text='Можешь сама накрутить сколько угодно))')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-creation_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


class PostParagraph(models.Model):
    """"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='paragraphs')
    title = models.CharField(max_length=500, null=True, blank=True, verbose_name='Подзаголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    position = models.IntegerField(default=1, verbose_name='Позиция')

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'
        ordering = ['position']

    def __str__(self):
        return self.title