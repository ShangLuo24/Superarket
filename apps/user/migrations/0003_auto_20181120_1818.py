# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20181120_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='username',
            name='password',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
    ]
