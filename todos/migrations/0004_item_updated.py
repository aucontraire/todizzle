# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_item_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]