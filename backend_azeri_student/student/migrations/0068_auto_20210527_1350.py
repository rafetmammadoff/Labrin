# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2021-05-27 13:50
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0067_auto_20210303_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('background_image', models.ImageField(null=True, upload_to=student.options.tools.get_about_cover)),
                ('summary', models.TextField()),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='blog_title',
            field=models.CharField(default='Blog yazıları', max_length=255),
        ),
    ]