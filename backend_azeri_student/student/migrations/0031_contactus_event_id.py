# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-10-31 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0030_auto_20181031_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='event_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]