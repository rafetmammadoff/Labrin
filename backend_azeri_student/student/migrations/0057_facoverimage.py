# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2021-01-25 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0056_faqquestion_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaCoverImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(null=True, upload_to='faq-cover')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
