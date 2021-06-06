# Generated by Django 3.2 on 2021-06-06 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0018_checkorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=100)),
                ('created', models.DateTimeField()),
                ('ended', models.DateTimeField()),
            ],
            options={
                'db_table': 'checkTag',
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='checkorder',
            name='cateogry_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='checkorder',
            name='product_name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='checkorder',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='check_order', to='api_v1.checktag'),
            preserve_default=False,
        ),
    ]
