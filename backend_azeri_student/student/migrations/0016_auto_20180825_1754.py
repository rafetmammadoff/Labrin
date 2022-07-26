# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-25 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_news_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitesetings',
            name='facebook_social_description',
            field=models.CharField(default='2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.', max_length=255),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='facebook_social_title',
            field=models.CharField(default='Azeristudent | You study, we care!', max_length=255),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='meta_description',
            field=models.TextField(default='2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.'),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='meta_keywords',
            field=models.CharField(default='Azeristudent | You study, we care!', max_length=300),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='social_image',
            field=models.ImageField(blank=True, null=True, upload_to=student.options.tools.get_country_cover),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='twitter_social_creator',
            field=models.CharField(default='@azeristudent01', max_length=255),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='twitter_social_image_alt',
            field=models.CharField(default='2008- ci ildən fəaliyyətə başlayan, 10 il iş təcrübəsinə malik, Azərbaycanın ən güvənilən xaricdə təhsil agentliyiyik.', max_length=255),
        ),
        migrations.AddField(
            model_name='websitesetings',
            name='twitter_social_site',
            field=models.CharField(default='@azeristudent01', max_length=255),
        ),
    ]
