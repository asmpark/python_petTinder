# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='followstruct',
            name='follow_user',
            field=models.CharField(default='', max_length=50),
        ),
    ]
