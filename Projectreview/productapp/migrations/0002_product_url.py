# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.CharField(default='brazilianscrub', max_length=1024),
            preserve_default=False,
        ),
    ]