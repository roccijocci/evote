# Generated by Django 2.0.7 on 2018-08-07 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_members_date_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='username',
            field=models.CharField(default=datetime.datetime(2018, 8, 7, 12, 47, 55, 995512, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]