# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-25 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0014_auto_20190125_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
