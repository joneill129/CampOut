# Generated by Django 3.1.6 on 2021-02-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='enddate',
            field=models.DateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='startdate',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]
