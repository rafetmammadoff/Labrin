# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-29 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0031_auto_20191213_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images', verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Images',
                'ordering': ('order',),
            },
        ),
    ]
