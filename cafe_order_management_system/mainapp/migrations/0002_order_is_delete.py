# Generated by Django 5.0 on 2025-03-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_delete',
            field=models.IntegerField(default=0, verbose_name='удалён'),
        ),
    ]
