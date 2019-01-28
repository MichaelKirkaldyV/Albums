# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-16 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0010_auto_20190116_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='misc_images', to='photography.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_photo', to='photography.Album'),
        ),
    ]
