# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-12-09 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0028_auto_20191209_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_logo', models.ImageField(upload_to=student.options.tools.get_uni_logo, verbose_name='Uni_logo')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Position')),
            ],
            options={
                'verbose_name': 'University in Exhibition',
                'verbose_name_plural': 'Universities in Exhibition',
                'ordering': ['position'],
            },
        ),
        migrations.AlterField(
            model_name='homecontent',
            name='home_content_type',
            field=models.IntegerField(choices=[(0, 'Bir kontentli'), (1, 'Proqramlar'), (2, 'Event Videolar'), (3, 'Contact form'), (4, 'Partners section'), (5, 'Universities')], default=0),
        ),
        migrations.AddField(
            model_name='homecontent',
            name='universities_from_previous_exhibtions',
            field=models.ManyToManyField(blank=True, to='partners.Universities'),
        ),
    ]
