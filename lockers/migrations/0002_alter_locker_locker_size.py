# Generated by Django 4.2.5 on 2023-10-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='locker_size',
            field=models.IntegerField(choices=[(1, 'Extra Small'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Extra Large')]),
        ),
    ]
