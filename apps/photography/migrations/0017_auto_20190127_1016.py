# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-27 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0016_auto_20190126_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='misc_image',
            field=models.ImageField(blank=True, null=True, upload_to='misc'),
        ),
    ]
