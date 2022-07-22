# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-16 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Country')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='season',
            field=models.IntegerField(choices=[(0, 'Qiş'), (1, 'Yaz'), (2, 'Yay'), (3, 'Payız')], default=0),
        ),
    ]