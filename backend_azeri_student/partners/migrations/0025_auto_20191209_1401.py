# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-09 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0024_auto_20191206_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
