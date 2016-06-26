# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coxinhaoupetralha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('geo', models.IntegerField()),
                ('potential', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=350, unique=True)),
                ('lat', models.DecimalField(decimal_places=14, max_digits=17)),
                ('lng', models.DecimalField(decimal_places=14, max_digits=17)),
            ],
        ),
    ]
