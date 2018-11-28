# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderForm', '0003_auto_20181128_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryaddress',
            old_name='province',
            new_name='harea',
        ),
        migrations.RenameField(
            model_name='deliveryaddress',
            old_name='district',
            new_name='hcity',
        ),
        migrations.RenameField(
            model_name='deliveryaddress',
            old_name='city',
            new_name='hproper',
        ),
        migrations.AlterField(
            model_name='orderinformation',
            name='orderState',
            field=models.SmallIntegerField(choices=[(4, '已完成'), (1, '退发货'), (0, '待付款'), (2, '待收货'), (3, '待评价')], default=0, verbose_name='订单状态'),
        ),
    ]
