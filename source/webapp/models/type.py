from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "types"
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
