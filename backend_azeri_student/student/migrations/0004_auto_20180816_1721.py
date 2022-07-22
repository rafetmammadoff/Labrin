# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-16 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_education_programs'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccommondationEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='educationprogram',
            options={'ordering': ('name',)},
        ),
    ]
