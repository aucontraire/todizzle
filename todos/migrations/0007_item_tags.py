# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0006_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='todos.Tag'),
        ),
    ]