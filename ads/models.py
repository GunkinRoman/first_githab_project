from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    price = models.PositiveBigIntegerField('Цена')
    publish_date = models.DateField('Дата публикации')

    class Meta:
        verbose_name = 'обьявления'
        verbose_name_plural = 'обьявления'
