# Generated by Django 3.2.9 on 2022-03-01 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_alter_compra_co_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='co_Total',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='costo total'),
        ),
    ]