# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-08 11:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0033_slidervideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citiestables',
            name='table_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='How many tables each city'),
        ),
    ]