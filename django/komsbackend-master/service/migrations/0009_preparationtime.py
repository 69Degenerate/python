# Generated by Django 3.2 on 2023-01-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_usersettings_stationid'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreparationTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('externalId', models.CharField(max_length=100)),
                ('tag', models.CharField(max_length=100)),
                ('preparation_time', models.IntegerField()),
            ],
        ),
    ]