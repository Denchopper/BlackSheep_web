# Generated by Django 3.2.15 on 2022-10-18 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_remove_beertype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='beertype',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]