# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-12 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_auto_20170810_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='firm_place',
            field=models.CharField(default='', max_length=255, verbose_name='公司省市'),
        ),
        migrations.AddField(
            model_name='firm',
            name='is_add',
            field=models.BooleanField(default=False, verbose_name='是否添加'),
        ),
        migrations.AddField(
            model_name='recruit',
            name='is_add',
            field=models.BooleanField(default=True, verbose_name='是否添加'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='release',
            field=models.DateField(verbose_name='发布日期'),
        ),
    ]
