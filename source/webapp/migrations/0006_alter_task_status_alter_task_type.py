# Generated by Django 5.0.6 on 2024-07-11 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_status_type_alter_task_status_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.type', verbose_name='Тип'),
        ),
    ]
