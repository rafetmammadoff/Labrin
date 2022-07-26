# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-12 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import student.options.fields


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0005_homepagebaseconfig_page_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerSays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Full name')),
                ('specialty', models.CharField(blank=True, max_length=250, null=True, verbose_name='Specialty')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='partners/says', verbose_name='Picture')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterFair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='Full name')),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
        migrations.AddField(
            model_name='eventvideo',
            name='event_date',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='eventvideo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='partner/event', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='eventvideo',
            name='youtube_link',
            field=student.options.fields.YoutubeLinkField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepagebaseconfig',
            name='page_url',
            field=models.CharField(default='/', help_text='Page url example /about/', max_length=255),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='partner_says',
            field=models.ManyToManyField(blank=True, to='partners.PartnerSays'),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='register_form',
            field=models.ManyToManyField(blank=True, to='partners.RegisterFair'),
        ),
    ]
