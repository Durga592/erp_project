# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FINANCE', '0002_auto_20180706_1331'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='modules',
            new_name='Module_Names',
        ),
    ]
