# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-15 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0002_on_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='taggeditem',
            name='created',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='is_published',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
