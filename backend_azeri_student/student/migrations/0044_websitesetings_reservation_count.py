# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-12 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0043_reservationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetings',
            name='reservation_count',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Reservation Count'),
        ),
    ]