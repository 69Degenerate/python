# Generated by Django 4.0.3 on 2023-01-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_alter_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.TextField(null=True),
        ),
    ]
