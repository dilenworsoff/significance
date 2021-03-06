# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_test_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='a_conversionrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='b_conversionrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='winner',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='test',
            name='a_conversions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='a_users',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='b_conversions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='test',
            name='b_users',
            field=models.IntegerField(default=0),
        ),
    ]
