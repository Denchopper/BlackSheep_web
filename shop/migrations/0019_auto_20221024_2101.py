# Generated by Django 3.2.15 on 2022-10-24 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20221024_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.RemoveField(
            model_name='beer',
            name='volume',
        ),
        migrations.AddField(
            model_name='beer',
            name='volume',
            field=models.ManyToManyField(to='shop.BeerVolume'),
        ),
    ]
