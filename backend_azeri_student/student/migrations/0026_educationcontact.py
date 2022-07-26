# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-07 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0025_galleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('univercity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Education')),
            ],
        ),
    ]
