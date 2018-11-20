from django import forms
from django.core.validators import RegexValidator

from user.models import Username


class AccountVerify(forms.Form):
    """
    AccountVerify: 账户注册验证
    """
    account = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$', "提示信息:手机号码格式错误"),
        ],
    )

    password1 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位以上的密码',
        'required': '请确认填写密码'
    }, min_length=6, required=True)

    password2 = forms.CharField(error_messages={
        'min_length': '请输入六位及六位的密码',
        'required': '请再次确认密码'
    }, min_length=6, required=True)

    def clean_account(self):
        data = self.cleaned_data
        one = Username.objects.filter(username=data.get('account')).first()
        print(one.password)
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
    )

    password = forms.CharField(error_messages={
        'min_length': '请输入六位及六位以上的密码',
        'required': '请确认填写密码'
    }, min_length=6, required=True)

    def clean_account(self):
        data = self.cleaned_data
        one = Username.objects.filter(username=data.get('account')).first()
        if one:
            return data.get('account')
        else:
            raise forms.ValidationError('账户不存在')

    # def clean(self):
    #     data = self.cleaned_data
    #     two = Username.objects.filter(username=data.get('account')).first()
    #     if two:
    #         raise forms.ValidationError({'password2': '密码必须一致'})
    #     else:
    #         return data
