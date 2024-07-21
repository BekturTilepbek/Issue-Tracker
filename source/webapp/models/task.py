from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    detailed_description = models.TextField(null=True, blank=True, default="", verbose_name='Подробное описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='tasks', verbose_name='Статус')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Типы', db_table='tasks_types')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
