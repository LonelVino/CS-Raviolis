# Generated by Django 3.2 on 2021-06-05 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0017_orderitem_gotten'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itm_price', models.FloatField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('gotten', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='check_order', to='api_v1.product')),
            ],
            options={
                'db_table': 'checkOrder',
            },
        ),
    ]
