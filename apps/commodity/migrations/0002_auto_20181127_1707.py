# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-27 17:07
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Activity_Describe',
            field=models.CharField(max_length=255, verbose_name='首页活动描述'),
        ),
        migrations.AlterField(
            model_name='create',
            name='Goods_spu_intro',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='商品详情'),
        ),
        migrations.AlterField(
            model_name='division',
            name='Division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Activity', verbose_name='专区id'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Goods_sku_Num',
            field=models.IntegerField(verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Goods_sku_Unitinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Unti', verbose_name='单位'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Goods_sku_cate_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Class', verbose_name='商品分类id'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Goods_sku_intro',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='商品简介'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='Goods_spu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Create', verbose_name='商品spu_id'),
        ),
        migrations.AlterField(
            model_name='home',
            name='Home_Imgurl',
            field=models.ImageField(upload_to='Home/%Y%m/%d', verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='Page_Imgurl',
            field=models.ImageField(upload_to='show/%Y%m/%d', verbose_name='图片地址'),
        ),
    ]
