# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-17 10:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0013_auto_20181117_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citiestables',
            name='cities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_cities_tables', to='partners.EventVideo'),
        ),
        migrations.AlterField(
            model_name='citiestables',
            name='table_count',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='How many tables each city'),
        ),
    ]
