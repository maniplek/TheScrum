# Generated by Django 3.2.12 on 2022-03-23 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0004_auto_20220323_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 6, 29, 644420), verbose_name='Date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='otp_generated_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 15, 6, 29, 644420)),
        ),
    ]