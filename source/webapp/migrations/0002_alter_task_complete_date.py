# Generated by Django 5.0.6 on 2024-06-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
    ]
