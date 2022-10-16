# Generated by Django 3.2.15 on 2022-10-16 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_beer_abv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snacktype',
            name='description',
        ),
        migrations.AlterField(
            model_name='beer',
            name='beer_style',
            field=models.ForeignKey(default='BEER', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.beerstyle'),
        ),
        migrations.AlterField(
            model_name='beer',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='beertype',
            name='name',
            field=models.CharField(default='No type', max_length=50),
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('type', models.ForeignKey(default='No_Type', on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.snacktype')),
            ],
        ),
    ]
