# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20171024_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='periodo_key',
        ),
        migrations.AddField(
            model_name='materia',
            name='url',
            field=models.URLField(default='/index.html'),
        ),
    ]
