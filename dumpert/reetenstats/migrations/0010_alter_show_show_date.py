# Generated by Django 3.2.12 on 2022-04-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reetenstats', '0009_alter_gast_gast_underline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='show_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
