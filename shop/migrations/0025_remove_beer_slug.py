# Generated by Django 3.2.15 on 2022-11-14 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20221107_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beer',
            name='slug',
        ),
    ]