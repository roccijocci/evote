# Generated by Django 2.0.7 on 2018-08-07 12:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='date_registered',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 7, 12, 25, 42, 307780, tzinfo=utc), verbose_name='date_registered'),
            preserve_default=False,
        ),
    ]
