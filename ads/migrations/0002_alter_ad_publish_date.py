# Generated by Django 4.2.4 on 2023-08-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='publish_date',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]