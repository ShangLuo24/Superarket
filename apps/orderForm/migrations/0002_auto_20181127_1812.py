# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-27 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'verbose_name': '收货地址', 'verbose_name_plural': '收货地址'},
        ),
        migrations.AlterModelOptions(
            name='orderinformation',
            options={'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
        migrations.AlterModelOptions(
            name='ordersgoods',
            options={'verbose_name': '订单商品', 'verbose_name_plural': '订单商品'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': '付款方式', 'verbose_name_plural': '付款方式'},
        ),
        migrations.AlterModelOptions(
            name='typeshipping',
            options={'verbose_name': '运输方式', 'verbose_name_plural': '运输方式'},
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='default',
            field=models.BooleanField(choices=[(1, '默认'), (0, '不默认')], default=0, verbose_name='默认地址'),
        ),
        migrations.AlterField(
            model_name='orderinformation',
            name='orderState',
            field=models.SmallIntegerField(choices=[(0, '待付款'), (4, '已完成'), (2, '待收货'), (3, '待评价'), (1, '退发货')], default=0, verbose_name='订单状态'),
        ),
        migrations.AlterModelTable(
            name='deliveryaddress',
            table='DeliveryAddress',
        ),
        migrations.AlterModelTable(
            name='orderinformation',
            table='OrderInformation',
        ),
        migrations.AlterModelTable(
            name='ordersgoods',
            table='OrdersGoods',
        ),
        migrations.AlterModelTable(
            name='payment',
            table='payment',
        ),
        migrations.AlterModelTable(
            name='typeshipping',
            table='TypeShipping',
        ),
    ]
