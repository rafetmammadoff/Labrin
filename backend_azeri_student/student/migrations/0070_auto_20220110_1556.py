# Generated by Django 3.1.7 on 2022-01-10 11:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import student.options.tools


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0069_merge_20210715_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('background_image', models.ImageField(null=True, upload_to=student.options.tools.get_about_cover)),
                ('summary', models.TextField()),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('video', models.FileField(upload_to='videos/')),
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
            name='video_title',
            field=models.CharField(default='Videolar', max_length=255),
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='student.country'),
        ),
        migrations.AlterField(
            model_name='reservationdate',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_reserve_date', to='student.education'),
        ),
        migrations.AlterField(
            model_name='schooltype',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_type', to='student.country'),
        ),
    ]
