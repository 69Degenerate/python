# Generated by Django 4.0.3 on 2023-01-19 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_alter_order_arrival_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='arrival_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
