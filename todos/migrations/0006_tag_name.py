# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
