# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-30 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0019_event_publish_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EducationProgram',
            new_name='LanguageProgram',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='programs',
            new_name='program_language',
        ),
    ]
