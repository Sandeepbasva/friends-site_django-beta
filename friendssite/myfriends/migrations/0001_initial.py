# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-14 15:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('birthday', models.DateField(default=datetime.date.today)),
                ('email', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('favouriteURL', models.URLField(blank=True)),
                ('description', models.TextField(blank=True, max_length=480)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
