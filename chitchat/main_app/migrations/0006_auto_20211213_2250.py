# Generated by Django 3.2.9 on 2021-12-13 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20211213_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 22, 50, 2, 123215)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 22, 50, 2, 122995)),
        ),
    ]
