# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0029_auto_20191209_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='universities',
            name='name',
            field=models.CharField(default='example name', max_length=255),
            preserve_default=False,
        ),
    ]
