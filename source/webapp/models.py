from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    detailed_description = models.TextField(null=True, blank=True, default="", verbose_name='Подробное описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks', verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', db_table='tasks_types')
    complete_date = models.DateField(verbose_name='Дата выполнения', null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Type(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "types"
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Status(models.Model):
    name = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "statuses"
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
