# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
