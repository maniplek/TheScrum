# Generated by Django 3.2.12 on 2022-03-23 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0002_auto_20220323_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 5, 22, 239039), verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_generated_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 5, 22, 239039)),
        ),
    ]
