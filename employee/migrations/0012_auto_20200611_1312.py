# Generated by Django 3.0.5 on 2020-06-11 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0011_auto_20200611_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='check_out',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
