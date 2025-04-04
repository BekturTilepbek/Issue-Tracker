# Generated by Django 5.0.6 on 2024-07-19 10:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_task_type_task_types'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete_date',
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
