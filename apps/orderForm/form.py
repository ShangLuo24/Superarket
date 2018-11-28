from django import forms
from django.core.validators import RegexValidator

from orderForm.models import DeliveryAddress


# 增加地址验证
class AddressAddForm(forms.Form):
    """
    用户添加收货地址的表单
    """
    userName = forms.CharField(
        error_messages={
            'required': '请填写用户名',
        }, required=True, max_length=50)

    telephone = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$', "手机号码格式错误"),
        ],
        error_messages={
            "required": "请填写电话号码",
        },
    )

    harea = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写省份',
        },
    )

    hproper = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写城市',
        },
    )

    hcity = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写区域',
        },
    )

    street = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写街道',
        },
    )

    inDetail = forms.CharField(
        required=True, max_length=255,
        error_messages={
            'required': '请确认填写详细地址',
        },
    )

    default = forms.BooleanField(
        required=False,
    )

    def clean(self):
        # 验证如果数据库里地址已经超过6六表报错
        # print(self.data.get("user_id"))
        count = DeliveryAddress.objects.filter(user_id=self.data.get("user_id")).count()
        if count >= 6:
            raise forms.ValidationError("收货地址最多只能保存6条")

        # 接收传入进来的值,获取到默认选项的值,进行判断
        apple = self.cleaned_data.get("default")
        print(apple)
        if apple:
            DeliveryAddress.objects.filter(user_id=self.data.get("user_id")).update(default=False)
        return self.cleaned_data


# 修改地址验证
class AlterAddForm(forms.Form):
    """
    用户添加收货地址的表单
    """
    userName = forms.CharField(
        error_messages={
            'required': '请填写用户名',
        }, required=True, max_length=50)

    telephone = forms.CharField(
        required=True,
        validators=[
            RegexValidator(r'^1[13456789]\d{9}$', "手机号码格式错误"),
        ],
        error_messages={
            "required": "请填写电话号码",
        },
    )

    harea = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写省份',
        },
    )

    hproper = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写城市',
        },
    )

    hcity = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写区域',
        },
    )

    street = forms.CharField(
        required=True, max_length=50,
        error_messages={
            'required': '请填写街道',
        },
    )

    inDetail = forms.CharField(
        required=True, max_length=255,
        error_messages={
            'required': '请确认填写详细地址',
        },
    )

    default = forms.BooleanField(
        required=False,
    )

    def clean(self):

        # 接收传入进来的值,获取到默认选项的值,进行判断
        apple = self.cleaned_data.get("default")
        print(apple)
        if apple:
            DeliveryAddress.objects.filter(user_id=self.data.get("user_id")).update(default=False)
        return self.cleaned_data
