# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-06 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='PRODUCT NAME')),
                ('technologies', models.CharField(max_length=250, verbose_name='TECHNOLOGIES')),
                ('client', models.CharField(max_length=250, verbose_name='CLIENT')),
            ],
        ),
    ]
