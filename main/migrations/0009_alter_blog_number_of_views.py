# Generated by Django 4.2.3 on 2023-07-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_blog_number_of_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='number_of_views',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Просмотры'),
        ),
    ]