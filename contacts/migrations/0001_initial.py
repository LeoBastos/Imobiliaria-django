# Generated by Django 3.2.6 on 2021-08-04 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200, verbose_name='Listing')),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=100, verbose_name='Contact Name')),
                ('email', models.CharField(max_length=100, verbose_name='Contact Email')),
                ('phone', models.CharField(max_length=100, verbose_name='Contact Phone')),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Contact Date')),
                ('user_id', models.IntegerField(blank=True, verbose_name='Contact User ID')),
            ],
        ),
    ]
