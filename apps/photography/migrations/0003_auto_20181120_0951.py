# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-20 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photography', '0002_auto_20181112_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='created_albums', to='photography.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_photo', to='photography.Album'),
        ),
    ]
