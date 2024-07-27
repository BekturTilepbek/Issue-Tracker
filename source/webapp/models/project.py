from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Project(models.Model):
    started_at = models.DateField(verbose_name='Дата начала')
    ended_at = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    users = models.ManyToManyField(User, related_name='projects', verbose_name='Пользователи', db_table='projects_users')

    def __str__(self):
        return f"{self.pk}. {self.name}: {self.started_at}"

    class Meta:
        db_table = "projects"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        permissions = [('add_user_in_project', 'Добавить пользователя в проект'),
                       ('delete_user_from_project', 'Удалить пользователя из проекта')]
