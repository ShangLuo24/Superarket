from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from orderForm.form import AddressAddForm, AlterAddForm
from orderForm.models import DeliveryAddress


# 添加地址
def address(request):
    """
    添加收货地址
    :param request:
    :return:
    """
    if request.method == 'POST':
        # 获取数据
        data = request.POST.dict()
        # 赋值id进行数量计算
        user_id = request.session.get("user_id")
        data['user_id'] = user_id
        # 处理数据,获得处理后的数据
        form = AddressAddForm(data)
        # 接收清理干净的数据
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # 手动添加必要参数
            cleaned_data['user_id'] = request.session.get("user_id")
            # 保存到数据库
            DeliveryAddress.objects.create(**cleaned_data)
            # 跳转页面
            return redirect("add:地址")
        else:
            # 如果格式不对或未填写,则返回报错内容,接收
            context = {
                'form': form,
            }
            # 渲染到页面
            return render(request, "orderForm/address.html", context)
    else:
        return render(request, "orderForm/address.html")


# 展示区
def gladd(request):
    """
    收货地址展示页
    :param request:
    :return:
    """
    if request.method == 'GET':
        user_id = request.session.get("user_id")
        if request.session.get("user_id") is None:
            # 没有登录跳转页面
            return redirect("user:登录")
        else:
            all = DeliveryAddress.objects.filter(user_id=user_id).order_by("-default")
            context = {
                'all': all,
            }
            return render(request, "orderForm/gladdress.html", context)
    else:
        return redirect("user:个人中心")


# 删除地址
def amendSite(request, id):
    """
    修改地址
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = request.POST.dict()
        # 赋值id进行数量计算
        user_id = request.session.get("user_id")
        data['user_id'] = user_id
        # 处理数据,获得处理后的数据
        form = AlterAddForm(data)
        # 接收清理干净的数据
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # 手动添加必要参数
            # cleaned_data['user_id'] = request.session.get("user_id")
            # 保存到数据库
            DeliveryAddress.objects.filter(user_id=user_id, pk=id).update(**cleaned_data)
            # 跳转展示页面
            return redirect("add:地址")
        else:
            # 如果格式不对或未填写,则返回报错内容,接收
            context = {
                'form': form,
            }
            # 渲染到页面
            return render(request, "orderForm/addadd.html", context)
    else:
        user_id = request.session.get("user_id")
        if request.session.get("user_id") is None:
            # 没有登录跳转页面
            return redirect("user:登录")
        else:
            try:
                all = DeliveryAddress.objects.get(user_id=user_id, pk=id)
            except DeliveryAddress.DoesNotExist:
                return redirect("add:地址")
            context = {
                'all': all,
            }
            return render(request, "orderForm/addadd.html", context)


# 删除地址
def deleteAlter(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        addId = request.POST.get('id')
        addId = int(addId)
        number = DeliveryAddress.objects.filter(user_id=user_id, pk=addId).delete()
        if number:
            return JsonResponse({'age': 0, 'clue': '删除成功'})
        else:
            return JsonResponse({'age': 1, 'clue': '删除失败'})
    else:
        if request.session.get("user_id") is None:
            # 没有登录跳转页面
            return redirect("user:登录")
        else:
            return redirect("add:地址")


# 更改默认地址
def Alter(request):
    if request.method == "POST":
        user_id = request.session.get("user_id")
        addId = request.POST.get('id')
        addId = int(addId)
        DeliveryAddress.objects.filter(user_id=user_id).update(default=False)
        number = DeliveryAddress.objects.filter(user_id=user_id, pk=addId).update(default=True)
        if number:
            return JsonResponse({'age': 2, 'clue': '修改成功'})
        else:
            return JsonResponse({'age': 3, 'clue': '修改失败'})
    else:
        if request.session.get("user_id") is None:
            # 没有登录跳转页面
            return redirect("user:登录")
        else:
            return redirect("add:地址")


# 提交订单
def submit(request):
    return render(request, 'orderForm/tureorder.html')


# 确认订单
def notarize(request):
    return render(request, 'orderForm/order.html')


# 订单详情
def orderForm(request):
    return  render(request, 'orderForm/allorder.html')