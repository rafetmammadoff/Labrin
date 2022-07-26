# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-01-27 17:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import student.options.fields
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0048_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplySettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events_first_title', models.CharField(max_length=100, verbose_name='First Title')),
                ('numune_field', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='First Title')),
                ('image', models.ImageField(upload_to=student.options.tools.get_exhibition_cover_path, verbose_name='Description Image')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Position')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='ConnectApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='main title')),
                ('start_date', models.DateTimeField(verbose_name='start data')),
                ('end_date', models.DateTimeField(verbose_name='end data')),
                ('image', models.ImageField(upload_to=student.options.tools.get_exhibition_cover_path, verbose_name='Main Image')),
                ('mape', student.options.fields.GoogleMapField(default='POINT (49.85115860712335 40.37782054099786)', max_length=255, verbose_name='Map')),
            ],
        ),
    ]
