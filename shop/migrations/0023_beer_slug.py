# Generated by Django 3.2.15 on 2022-11-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_alter_beer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]