# Generated by Django 5.0 on 2025-03-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_order_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_delete',
        ),
        migrations.AddField(
            model_name='order',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]
