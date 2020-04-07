# Generated by Django 3.0.2 on 2020-04-06 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reetenstats', '0003_auto_20200407_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating_video',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='reetenstats.Video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gast',
            name='gast_age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
