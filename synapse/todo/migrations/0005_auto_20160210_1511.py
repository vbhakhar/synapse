# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 15:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20160210_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_item',
            name='children',
        ),
        migrations.RemoveField(
            model_name='list_item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='list_item',
            name='profile',
        ),
        migrations.DeleteModel(
            name='list_item',
        ),
        migrations.DeleteModel(
            name='user_profile',
        ),
    ]
