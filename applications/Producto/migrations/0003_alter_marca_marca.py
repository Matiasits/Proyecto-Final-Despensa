# Generated by Django 3.2 on 2022-11-25 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_auto_20221125_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='marca',
            field=models.CharField(default='coca cola', max_length=50, verbose_name='Marca'),
        ),
    ]
