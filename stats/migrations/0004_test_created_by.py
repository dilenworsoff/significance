# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 06:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0003_auto_20171125_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='created_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
