# Generated by Django 3.2.15 on 2022-10-18 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_brewery_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='snacktype',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]