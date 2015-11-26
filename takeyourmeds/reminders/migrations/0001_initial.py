# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2015-11-16 09:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(choices=[(b'cron', 10), (b'manual', 20)])),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
            options={
                'ordering': ('-created',),
                'get_latest_by': 'created',
            },
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=100)),
                ('audio_url', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
                ('last_run', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='times', to='reminders.Reminder')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.AddField(
            model_name='instance',
            name='reminder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='reminders.Reminder'),
        ),
        migrations.AlterUniqueTogether(
            name='time',
            unique_together=set([('reminder', 'time')]),
        ),
    ]
