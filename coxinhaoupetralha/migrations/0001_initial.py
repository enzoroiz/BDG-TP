# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_Petralha', models.BooleanField()),
                ('text', models.CharField(max_length=350, unique=True)),
                ('lat', models.DecimalField(decimal_places=14, max_digits=17)),
                ('lng', models.DecimalField(decimal_places=14, max_digits=17)),
            ],
        ),
    ]
