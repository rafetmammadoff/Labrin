# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-25 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20180825_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websitesetings',
            name='meta_description',
            field=models.TextField(default='2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.', editable=False),
        ),
        migrations.AlterField(
            model_name='websitesetings',
            name='meta_keywords',
            field=models.CharField(default='Azeristudent | You study, we care!', editable=False, max_length=300),
        ),
    ]
