# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_tag_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
