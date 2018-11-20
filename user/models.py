from django.db import models


class Username(models.Model):
    username = models.CharField(max_length=11)  # 用户名
    nickname = models.CharField(max_length=20, null=True)  # 昵称
    telephone = models.CharField(max_length=11, null=True)  # 电话
    password = models.CharField(max_length=16)  # 密码
    sex_choices = (
        (1, '男'),
        (2, '女'),
    )
    sex = models.SmallIntegerField(choices=sex_choices, default=1)  # 性别
    birthday = models.DateField(auto_now=False, null=True)  # 生日
    location = models.CharField(max_length=50, null=True)  # 地址
    Create_time = models.DateTimeField(auto_now_add=True)  # 注册日期
    Update_time = models.DateTimeField(auto_now=True)  # 修改日期

    class Meta:
        db_table = 'username'

    def __str__(self):
        return self.username
