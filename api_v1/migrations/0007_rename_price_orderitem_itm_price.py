# Generated by Django 3.2 on 2021-06-04 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0006_rename_price_userorder_usr_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='price',
            new_name='itm_price',
        ),
    ]
