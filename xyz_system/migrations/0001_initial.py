# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-02-03 15:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import xyz_util.modelutils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='as_system_master', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': '\u7ba1\u7406\u5458',
                'verbose_name_plural': '\u7ba1\u7406\u5458',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('logo', models.URLField(blank=True, null=True, verbose_name='Logo\u5730\u5740')),
                ('role_model_map', xyz_util.modelutils.JSONField(blank=True, default={}, verbose_name='\u89d2\u8272\u6743\u9650')),
                ('settings', xyz_util.modelutils.JSONField(verbose_name='\u914d\u7f6e')),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf',
                'verbose_name_plural': '\u7cfb\u7edf',
            },
        ),
    ]
