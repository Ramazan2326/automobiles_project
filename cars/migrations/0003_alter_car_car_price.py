# Generated by Django 4.2.2 on 2023-06-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20230622_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_price',
            field=models.CharField(max_length=50, verbose_name='стоимость автомобиля'),
        ),
    ]
