# Generated by Django 3.0.5 on 2020-06-12 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_city_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='employeeprofile',
            name='state',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]