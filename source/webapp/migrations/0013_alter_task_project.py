# Generated by Django 5.0.6 on 2024-07-21 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20240721_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.project', verbose_name='Проект'),
        ),
    ]
