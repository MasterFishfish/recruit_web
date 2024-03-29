# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-03 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(default='http', max_length=255, verbose_name='代理类型')),
                ('addr', models.CharField(max_length=255, verbose_name='代理地址')),
                ('is_alive', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_http_and_https', models.BooleanField(default=False, verbose_name='是否包含所有协议')),
            ],
        ),
    ]
