# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-07 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0023_auto_20180907_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='accommondation',
            field=models.ManyToManyField(blank=True, to='student.AccommondationEducation'),
        ),
        migrations.AlterField(
            model_name='education',
            name='city',
            field=models.ManyToManyField(blank=True, to='student.City'),
        ),
        migrations.AlterField(
            model_name='education',
            name='program_language',
            field=models.ManyToManyField(blank=True, to='student.LanguageProgram'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school_type',
            field=models.ManyToManyField(blank=True, to='student.SchoolType'),
        ),
        migrations.AlterField(
            model_name='education',
            name='secondary_program',
            field=models.ManyToManyField(blank=True, to='student.SecondaryProgram'),
        ),
        migrations.AlterField(
            model_name='education',
            name='specials',
            field=models.ManyToManyField(blank=True, to='student.HigherSpecial'),
        ),
        migrations.AlterField(
            model_name='education',
            name='univercity_program',
            field=models.ManyToManyField(blank=True, to='student.UnivercityProgram'),
        ),
    ]
