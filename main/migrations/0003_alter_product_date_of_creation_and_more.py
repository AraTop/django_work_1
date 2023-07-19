# Generated by Django 4.2.3 on 2023-07-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.TimeField(blank=True, null=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.TimeField(blank=True, null=True, verbose_name='дата последнего изменения'),
        ),
    ]
