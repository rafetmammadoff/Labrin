# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-19 09:31
from __future__ import unicode_literals

from django.db import migrations, models
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0022_auto_20190318_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=student.options.tools.get_slider_image),
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='left_or_right',
            field=models.IntegerField(blank=True, choices=[(0, 'Left'), (1, 'Right')], null=True),
        ),
    ]
