# Generated by Django 3.2 on 2021-06-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AlterModelTable(
            name='order',
            table='Order',
        ),
        migrations.AlterModelTable(
            name='orderitem',
            table='OrderItem',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Product',
        ),
    ]
