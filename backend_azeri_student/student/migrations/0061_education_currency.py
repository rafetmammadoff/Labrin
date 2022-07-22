# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-12-28 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0060_currencies'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='student.currencies'),
        ),
    ]
