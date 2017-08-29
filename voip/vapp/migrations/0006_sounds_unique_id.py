# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 02:00
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0005_auto_20170730_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='sounds',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]