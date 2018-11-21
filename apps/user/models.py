from django.db import models

from db.base_model import BaseModel


class Username(BaseModel):
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    username = models.CharField(max_length=11, verbose_name='用户名')  # 用户名
    nickname = models.CharField(max_length=50, null=True, blank=True, verbose_name='昵称')  # 昵称
    telephone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话号码')  # 电话
    password = models.CharField(max_length=32, verbose_name='密码')  # 密码
    sex = models.SmallIntegerField(choices=sex_choices, default=1, verbose_name='性别')  # 性别
    birthday = models.DateField(auto_now=False, null=True, blank=True, verbose_name='生日')  # 生日
    school = models.CharField(max_length=50, null=True, blank=True, verbose_name='学校')  # 学校
    nativePlace = models.CharField(max_length=50, null=True, blank=True, verbose_name='家乡')  # 家乡
    location = models.CharField(max_length=50, null=True, blank=True, verbose_name='地址')  # 地址

    class Meta:
        db_table = 'username'
        verbose_name = '用户表'

    def __str__(self):
        return self.username
