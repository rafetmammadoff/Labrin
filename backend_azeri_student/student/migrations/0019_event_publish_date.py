# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-29 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20180827_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]