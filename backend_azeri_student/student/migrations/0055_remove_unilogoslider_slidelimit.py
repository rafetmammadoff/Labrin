# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-12-08 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0054_auto_20201208_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unilogoslider',
            name='slideLimit',
        ),
    ]
