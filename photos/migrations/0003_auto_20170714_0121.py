# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20170714_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]