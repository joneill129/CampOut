# Generated by Django 3.1.6 on 2021-02-09 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210208_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campground',
            name='directions',
        ),
    ]