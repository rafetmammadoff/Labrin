# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-27 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0047_auto_20190710_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='special_events', verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
