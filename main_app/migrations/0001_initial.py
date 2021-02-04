# Generated by Django 3.1.6 on 2021-02-04 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('address', models.CharField(default='', max_length=100)),
                ('zipcode', models.CharField(default='', max_length=15)),
                ('directions', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('campground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.campground')),
            ],
        ),
    ]
