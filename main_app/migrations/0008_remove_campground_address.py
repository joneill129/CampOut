# Generated by Django 3.1.6 on 2021-02-09 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_remove_campground_directions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campground',
            name='address',
        ),
    ]
