# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2021-01-18 08:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0054_auto_20210116_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqanswer',
            name='question',
        ),
        migrations.DeleteModel(
            name='faqAnswer',
        ),
    ]
