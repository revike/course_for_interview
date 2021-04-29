from django.db import models


class GoodItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Создано')  # auto_now=True
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    price = models.DecimalField(
        default=0, max_digits=8, decimal_places=2, verbose_name='Цена')
    vendor = models.CharField(max_length=255, verbose_name='Поставщик')

    def __str__(self):
        return f'{self.title} - {self.price}'

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточки товаров'
