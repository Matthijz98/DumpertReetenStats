# Generated by Django 3.2.12 on 2022-04-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reetenstats', '0007_auto_20220426_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_dumpert_id',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='show_youtube_id',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
