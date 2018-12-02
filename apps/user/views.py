import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from user.form import AccountVerify, RegisterLogin, ForgetPass, PersonalInformation
from user.helper import set_password, old_request, set_session, send_sms
from user.models import Username
import re
import random
from django_redis import get_redis_connection


def reg(request):
    """
    用户注册,
    获取数据
    解析数据
    返回响应
    :param request:
    :return:
    """
    if request.method == 'POST':  # 判断是从什么条件下进入网页,如果是POST,则是提交的方式
        data = request.POST  # 获取提交内容
        form = AccountVerify(data)  # 解析提交内容
        if form.is_valid():  # 对获取清除后的数据判断
            data = form.cleaned_data
            password_one = data['password2']
            password = set_password(password_one)
            Username.objects.create(username=data['account'], password=password)  # 存入数据库
            return redirect("user:登录")
        else:
            context = {
                'errors': form.errors,  # 生成错误提示
                'data': data,  # 回显数据
            }
            # print(data.get('account'))
            return render(request, "personal/reg.html", context)  # 提交到页面
    else:
        return render(request, 'personal/reg.html')


def message(request):
    """
    发送短信验证码
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 接收手机号码,生成随机码,保存在redis中,
        phone = request.POST.get('account', '')
        # 后台验证手机号码格式
        phone_one = re.compile("^1[3-9]\d{9}$")
        # 进行匹配
        result = re.search(phone_one, phone)
        if not result:
            return JsonResponse({"errr": 1, "errorore": "请求方式错误"})
        else:
            # 验证成功,则生成随机数
            random_code = "".join([str(random.randint(0, 9)) for _ in range(4)])
            # 保存在redis中,设置过期时间
            red = get_redis_connection("default")
            red.set(phone, random_code)
            red.expire(phone, 120)
            # 发送短信
            # print(random_code)
            __business_id = uuid.uuid1()
            params = "{\"code\":\"%s\",\"product\":\"测试验证\"}" % random_code
            print(send_sms(__business_id, phone, "注册验证", "SMS_2245271", params))
            return JsonResponse({"errr": 0})
    else:
        return JsonResponse({"errr": 1, "errorore": "请求方式错误"})


def login(request):
    """
    用户登录,
    获取数据
    解析数据
    返回响应
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 接收数据
        data = request.POST
        form = RegisterLogin(data)
        if form.is_valid():
            # 接收清除后的数据
            data = form.cleaned_data
            password_one = data['password']
            password = set_password(password_one)
            one = Username.objects.filter(username=data['account']).first()
            # 判断保存密码是否相同
            if one.password == password:
                set_session(request, one)
                # 判断是从哪里跳转过来的
                next = request.GET.get("next")
                if next:
                    return redirect(next)
                else:
                    return redirect("com:首页")
            else:
                context = {
                    'errors': '密码错误'
                }
                return render(request, 'personal/login.html', context)
        else:
            context = {
                'errors': form.errors,
                'data': data,
            }
            return render(request, 'personal/login.html', context)
    else:
        return render(request, 'personal/login.html')


def forget_password(request):
    """
    修改密码,获取input内容
    获取数据
    解析数据
    返回响应
    :param request:
    :return:
    """
    if request.method == 'POST':  # 判断是从什么条件下进入网页,如果是POST,则是提交的方式
        data = request.POST  # 获取提交内容
        form = ForgetPass(data)  # 解析提交内容
        if form.is_valid():  # 对获取清除后的数据判断
            data = form.cleaned_data
            password_one = data['password2']
            password = set_password(password_one)
            Username.objects.filter(username=data['account']).update(password=password)  # 存入数据库
            return redirect("user:登录")
        else:
            context = {
                'errors': form.errors,  # 生成错误提示
                'data': data,  # 回显数据
            }
            # print(data.get('account'))
            return render(request, "personal/forgetpassword.html", context)  # 提交到页面
    else:
        return render(request, 'personal/forgetpassword.html')


@old_request
def member(request):
    """
    个人中心
    :param request:
    :return:
    """
    user_id = request.session.get("user_id")
    data = Username.objects.filter(pk=user_id).first()
    head = request.session.get("user_head")
    if data.nickname is None:
        context = {
            'user_nickname': data.username,
            'user_head': head,
        }
        return render(request, 'personal/member.html', context)
    else:
        context = {
            'user_nickname': data.nickname,
            'user_head': head,
        }
        return render(request, 'personal/member.html', context)


@old_request
def infor(request):
    """
    个人信息
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 获取数据
        data = request.POST
        head = request.FILES.get('head')
        # 处理数据
        form = PersonalInformation(data)
        if form.is_valid():
            # 接收处理过后的数据
            data = form.cleaned_data
            user_id = request.session.get("user_id")
            # 查询session保存的id,然后通过id添加数据
            # print(type(data['telephone']))
            sex = request.POST.get("sex")

            Username.objects.filter(pk=user_id).update(nickname=data['nickname'],
                                                       telephone=data['telephone'],
                                                       sex=sex,
                                                       birthday=data['birthday'],
                                                       school=data['school'],
                                                       nativePlace=data['nativePlace'],
                                                       location=data['location'],
                                                       )
            # 回显数据
            data = Username.objects.get(pk=user_id)
            data.head = head
            data.save()
            set_session(request, data)
            head = request.session.get("user_head")
            print(head)
            data2 = Username.objects.get(pk=user_id)
            context = {
                'data': data2
            }
            return render(request, 'personal/infor.html', context)
        else:
            context = {
                'errors': form.errors,  # 生成错误提示
            }
            return render(request, 'personal/infor.html', context)
    else:
        # 查询session保存的id,查询数据
        user_id = request.session.get("user_id")
        data = Username.objects.filter(pk=user_id).first()
        # 回显数据
        context = {
            'data': data
        }
        return render(request, 'personal/infor.html', context)


@old_request
def delete(request):
    request.session.clear()
    return redirect("user:登录")
