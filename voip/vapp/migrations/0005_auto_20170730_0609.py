# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0004_auto_20170730_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numobject',
            name='ident',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]