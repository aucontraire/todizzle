# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
