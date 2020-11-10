from django.db import models


class Bitcoin(models.Model):
    price = models.DecimalField(max_digits=17, decimal_places=11, verbose_name=u'Цена')
    last_updated = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.price
