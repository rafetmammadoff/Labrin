# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-21 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0028_auto_20180915_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoReplyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='educationcontenttype',
            name='edu_type',
            field=models.IntegerField(choices=[(0, 'Bir kontentli'), (1, 'Iki kontentli'), (2, 'Əlaqə bölməsi'), (3, 'Xəritə bölməsi'), (4, 'Qalareya bölməsi')], default=0),
        ),
    ]