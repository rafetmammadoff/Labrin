# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-15 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0034_auto_20181220_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetings',
            name='successful_cover',
            field=models.ImageField(blank=True, null=True, upload_to=student.options.tools.get_successful_cover),
        ),
    ]