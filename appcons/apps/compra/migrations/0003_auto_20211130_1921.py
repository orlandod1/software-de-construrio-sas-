# Generated by Django 3.2 on 2021-12-01 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_auto_20211122_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='co_Total',
            field=models.PositiveIntegerField(max_length=11, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='compra',
            name='co_fechaIngreso',
            field=models.DateField(),
        ),
    ]
