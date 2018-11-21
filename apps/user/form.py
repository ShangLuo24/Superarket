from django import forms
from django.core.validators import RegexValidator
from datetime import date
from user.models import Username


class AccountVerify(forms.Form):
    """
    AccountVerify: 账户注册验证
    """
    account = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$',
                           "提示信息:手机号码格式错误"),
        ],
    )

    password1 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位以上的密码',
        'required': '请确认填写密码'
    }, min_length=6, max_length=16, required=True)

    password2 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位的密码',
        'max_length': '请输入16位以内的密码',
        'required': '请再次确认密码'
    }, min_length=6, max_length=16, required=True)

    def clean_account(self):
        data = self.cleaned_data
        one = Username.objects.filter(username=data.get('account')).first()
        # print(one.password)
        if one:
            raise forms.ValidationError('账户已存在')
        else:
            return data.get('account')

    def clean(self):
        data = self.cleaned_data
        if data.get('password2') != data.get('password1'):
            raise forms.ValidationError({'password2': '密码必须一致'})
        return data


class RegisterLogin(forms.Form):
    """
    RegisterLogin: 验证账号登录
    """
    account = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$', "提示信息:手机号码格式错误"),
        ],
        error_messages={
            "required": "请填写账号",
        },
    )

    password = forms.CharField(error_messages={
        'min_length': '请输入六位及六位以上的密码',
        'max_length': '请输入16位以内的密码',
        'required': '请确认填写密码'
    }, min_length=6, max_length=16, required=True)

    def clean_account(self):
        data = self.cleaned_data
        one = Username.objects.filter(username=data.get('account')).first()
        if one:
            return data.get('account')
        else:
            raise forms.ValidationError('账户不存在')


class ForgetPass(forms.Form):
    """
    AccountVerify: 用户修改密码
    """
    account = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$',
                           "提示信息:手机号码格式错误"),
        ],
    )

    password1 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位以上的密码',
        'max_length': '请输入16位以内的密码',
        'required': '请确认填写密码'
    }, min_length=6, max_length=16, required=True)

    password2 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位的密码',
        'max_length': '请输入16位以内的密码',
        'required': '请再次确认密码'
    }, min_length=6, max_length=16, required=True)

    def clean(self):
        data = self.cleaned_data
        if data.get('password2') != data.get('password1'):
            raise forms.ValidationError({'password2': '密码必须一致'})
        return data


class PersonalInformation(forms.Form):
    """
    验证个人信息合格性
    """
    nickname = forms.CharField(error_messages={
        'max_length': '昵称长度必须小于16位',
    }, required=False)  # 昵称

    telephone = forms.CharField(validators=[
        RegexValidator(r'^1[13456789]\d{9}$',
                       "提示信息:手机号码格式错误"),
    ], required=False)  # 电话号码

    birthday = forms.CharField(required=False)  # 出生日期

    school = forms.CharField(validators={
        'max_length': '地址长度必须小于50位',
    }, required=False)  # 学校

    nativePlace = forms.CharField(validators={
        'max_length': '地址长度必须小于50位',
    }, required=False)  # 现地址

    location = forms.CharField(validators={
        'max_length': '地址长度必须小于50位',
    }, required=False)  # 家乡地址

    def clean_time(self):
        # 获取当前时间
        now = date.today()
        # 获取文本时间
        time = self.cleaned_data.get('birthday')
        # print(time, not time)
        if time > now:
            raise forms.ValidationError('请正确填写日期')
        return time
