# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-13 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0030_universities_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerfair',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='registerfair',
            name='last_name',
        ),
    ]