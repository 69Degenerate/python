# Generated by Django 4.1 on 2022-10-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_moviesinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesinfo',
            name='release_year',
            field=models.CharField(max_length=122),
        ),
    ]
