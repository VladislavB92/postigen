# Generated by Django 4.2.5 on 2023-10-03 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0002_alter_parcel_parcel_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='parcel_size',
            new_name='size',
        ),
    ]