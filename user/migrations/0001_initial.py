# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('telephone', models.CharField(max_length=11, null=True)),
                ('password', models.CharField(max_length=16)),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1)),
                ('birthday', models.DateField(null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('Create_time', models.DateTimeField(auto_now_add=True)),
                ('Update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'name',
            },
        ),
    ]