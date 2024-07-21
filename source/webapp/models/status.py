from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "statuses"
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
    