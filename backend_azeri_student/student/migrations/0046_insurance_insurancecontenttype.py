# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-07-10 12:16
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import student.options.fields


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0045_auto_20190312_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.IntegerField(choices=[(0, 'Content type 1'), (1, 'Content type 2')], default=0)),
                ('order', models.IntegerField(default=0, help_text='Kontentin sıralanma yerini təyin edir', verbose_name='Sırası')),
                ('title_1', models.CharField(blank=True, help_text='1 No-lu kontent üçün başlıq', max_length=255, null=True)),
                ('content_1', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title_2', models.CharField(blank=True, help_text='2 No-lu kontent üçün başlıq', max_length=255, null=True)),
                ('youtube_video', student.options.fields.YoutubeLinkField(help_text='2 No-lu kontent üçün video')),
                ('content_2', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Insurance')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]