# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-11 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_auto_20181112_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCopyright',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='&copy; AZERISTUDENT. ALL RIGHTS RESERVED.', max_length=255)),
            ],
        ),
    ]
