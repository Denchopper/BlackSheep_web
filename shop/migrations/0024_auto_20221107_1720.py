# Generated by Django 3.2.15 on 2022-11-07 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_beer_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snack',
        ),
        migrations.DeleteModel(
            name='SnackType',
        ),
    ]
