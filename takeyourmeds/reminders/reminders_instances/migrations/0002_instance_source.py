# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-14 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders_instances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='source',
            field=models.IntegerField(choices=[(b'manual', 10), (b'schedule', 20)], default=10),
            preserve_default=False,
        ),
    ]
