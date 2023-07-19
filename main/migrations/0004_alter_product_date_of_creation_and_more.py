# Generated by Django 4.2.3 on 2023-07-19 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='дата последнего изменения'),
            preserve_default=False,
        ),
    ]
