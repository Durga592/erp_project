# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FINANCE', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='finance',
            new_name='modules',
        ),
    ]
