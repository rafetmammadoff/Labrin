# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-12-23 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0051_remove_reservationdate_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='faqAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaqQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_content', models.CharField(max_length=400, null=True)),
                ('questionicon', models.CharField(max_length=40, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='FaqQuestionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faqfor', models.CharField(max_length=150, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='faqquestion',
            name='faqfor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.FaqQuestionType'),
        ),
        migrations.AddField(
            model_name='faqanswer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.FaqQuestion'),
        ),
    ]
