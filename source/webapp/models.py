from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=50, null=False, blank=False, default="new", choices=status_choices, verbose_name='Статус')
    complete_date = models.DateField(verbose_name="Дата выполнения", null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
