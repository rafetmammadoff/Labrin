# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2021-01-16 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0053_auto_20201223_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqquestiontype',
            name='questionicon',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]