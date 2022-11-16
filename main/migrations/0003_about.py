# Generated by Django 3.2.15 on 2022-11-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_event_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=10)),
                ('e_mail', models.EmailField(max_length=254)),
                ('insta_page', models.URLField()),
            ],
        ),
    ]
