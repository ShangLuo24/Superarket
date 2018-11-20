from django.shortcuts import render, redirect
from django.http import HttpResponse

from user.form import AccountVerify, RegisterLogin
from user.models import Username


def reg(request):
    """
    用户注册,
    获取数据
    解析数据
    返回响应
    :param request:
    :return:
    """
    # Username.objects.create(username='shangshan24', password='1013144')
    if request.method == 'POST':    # 判断是从什么条件下进入网页,如果是POST,则是提交的方式
        data = request.POST        # 获取提交内容
        form = AccountVerify(data)  # 解析提交内容
        if form.is_valid():       # 对获取清除后的数据判断
            data = form.cleaned_data
            # print(data)
            Username.objects.create(username=data['account'], password=data['password2'])   # 存入数据库
            return redirect("user:首页")
        else:
            context = {
                'errors': form.errors,   # 生成错误提示
                'data': data,      # 回显数据
            }
            # print(data.get('account'))
            return render(request, "personal/reg.html", context)   # 提交到页面
    else:
        return render(request, 'personal/reg.html')


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
        data = request.POST
        form = RegisterLogin(data)
        if form.is_valid():
            data = form.cleaned_data
            one = Username.objects.filter(username=data['account'])
            print(one)
            return redirect("user:首页")
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
    return render(request, 'personal/forgetpassword.html')


def index(request):
    return render(request, 'father/index.html')
