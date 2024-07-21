from django.db import models


class Project(models.Model):
    started_at = models.DateField(verbose_name='Дата начала')
    ended_at = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.pk}. {self.name}: {self.started_at}"

    class Meta:
        db_table = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
