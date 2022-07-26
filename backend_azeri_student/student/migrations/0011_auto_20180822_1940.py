# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-22 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20180821_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='educationcategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
