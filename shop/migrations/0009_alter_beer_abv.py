# Generated by Django 3.2.15 on 2022-10-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_beer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='abv',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
