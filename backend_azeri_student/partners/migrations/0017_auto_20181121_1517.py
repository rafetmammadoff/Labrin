# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-21 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0016_registerfair_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerfair',
            name='invoice_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Invoice number'),
        ),
    ]
