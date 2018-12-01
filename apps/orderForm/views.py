from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django_redis import get_redis_connection
import random
from commodity.models import Goods
from orderForm.form import AddressAddForm, AlterAddForm
from orderForm.models import DeliveryAddress, TypeShipping, OrderInformation, OrdersGoods
from user.helper import old_request


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


# 先确认订单
@old_request
def submit(request):
    if request.method == "POST":
        return redirect('shop:购物车')
    else:
        # 获取登录用户的id
        user_id = request.session.get("user_id")
        # 获取地址
        Address = DeliveryAddress.objects.filter(is_delete=False).order_by('-default').first()
        # 获取商品id,建立radis链接
        user_id = "User_{}".format(user_id)
        cnn = get_redis_connection('default')
        sku_ids = request.GET.getlist("sku_id")
        # print(sku_ids)
        goods = []
        allprice = 0
        for sku_id in sku_ids:
            try:
                sku_id = int(sku_id)
            except:
                return redirect("shop:购物车")
            # 根据id 查询商品Goods
            good = Goods.objects.get(pk=sku_id, is_delete=False)
            goods.append(good)
            # 根据id,查询数量
            count = cnn.hget(user_id, sku_id)
            count = int(count)
            good.count = count
            # 商品总价格
            price = count * good.Goods_sku_Price
            allprice += price
        # print(goods)
        # 查询运输方式
        carriage = TypeShipping.objects.all().order_by('transitCharge')
        # 渲染到页面
        contxet = {
            'Address': Address,
            'Goods': goods,
            'carriage': carriage,
            'allprice': allprice,
        }
        return render(request, 'orderForm/tureorder.html', contxet)


# 后提交订单
@old_request
def notarize(request):
    # 接收传递过来的订单信息,查询数据库信息
    orderNum = request.GET.get("orderNum")
    order = OrderInformation.objects.get(orderNum=orderNum)
    # 计算总金额
    sku_price = order.orderPrice
    transit_price_Key = order.transit_price_Key
    price = sku_price + transit_price_Key

    goods = order.ordersgoods_set.all()
    for one in goods:
        one.goodsPrice
    contxet ={
        "order": order,
        'price': price
    }
    return render(request, 'orderForm/order.html', contxet)


# 存储确认后的订单信息
def seve(request):
    if request.method == 'POST':
        user_id = request.session.get("user_id")
        # 接收传递过来的地址id, 商品id, 运输方式id
        address_id = request.POST.get("address")
        sku_ids = request.POST.getlist("sku_id")
        carriage_id = request.POST.get("carriage")

        # 判断地址id是否是整数
        try:
            address_id = int(address_id)
        except:
            return JsonResponse({"age": 1, "matter": '地址参数错误'})
        # 查询地址id是否存在
        try:
            address = DeliveryAddress.objects.get(pk=address_id)
        except DeliveryAddress.DoesNotExist:
            return JsonResponse({"age": 2, "matter": '地址不存在'})

        # 判断商品id是否是整数
        try:
            sku_intid = [int(sku_id) for sku_id in sku_ids]
        except:
            return JsonResponse({"age": 3, "matter": '商品参数错误'})

        # 判断商品是否存在
        for sku_id in sku_intid:
            try:
                Goods.objects.get(pk=sku_id)
            except Goods.DoesNotExist:
                return JsonResponse({"age": 4, "matter": '商品不存在'})

        # 判断运输方式id是否是整数
        try:
            carriage_id = int(carriage_id)
        except:
            return JsonResponse({"age": 5, "matter": '运输参数错误'})

        # 判断运输方式是否存在
        try:
            shopp = TypeShipping.objects.get(pk=carriage_id)
        except TypeShipping.DoesNotExist:
            return JsonResponse({"age": 6, "matter": '运输方式不存在'})

        # 保存数据到订单信息表内,先准备需要的字段的值
        #
        #     订单金额
        #     用户ID
        #     收货人姓名
        #     收货人电话
        #     收货地址id
        #     订单状态
        #     运输方式
        #     付款id
        #     实付金额

        # 订单编号:随机在A-Z中选取一个大写英文字母 大写字母,年月日,随机数
        try:
            number = "{}{}{}".format(datetime.now().strftime('%Y%m%d%H%M%S'), user_id, (random.randint(10000, 99999)))
        except:
            return JsonResponse({"age": 7, "matter": '生成订单号错误'})
        # 用户ID
        # print(orderNum)
        # UserKey = user_id
        # # 收货人姓名
        # UserName = address.userName
        # # 收货人电话
        # Telephone = address.telephone
        # # 收货地址id
        # AddressKey = address.pk
        # # 运输方式
        # transitKey = shopp.transit
        # # 运输价格
        # transit_price_Key = shopp.transitCharge
        # print(number)
        # print(UserKey)
        # print(UserName)
        # print(Telephone)
        # print(AddressKey)
        # print(transitKey)
        # print(transit_price_Key)

        # 保存数值
        try:
            information = OrderInformation.objects.create(
                orderNum=number,
                UserKey_id=user_id,
                UserName=address.userName,
                Telephone=address.telephone,
                AddressKey_id=address.pk,
                transitKey=shopp.transit,
                transit_price_Key=shopp.transitCharge,
            )
        except:
            return JsonResponse({"age": 8, "matter": '保存订单信息出错'})

        # 链接radis
        try:
            # 建立连接
            cnn = get_redis_connection('default')
            # 准备key
            user_id = "User_{}".format(user_id)
        except:
            return JsonResponse({"age": 9, "matter": '建立radis错误'})
        # 准备总金额
        allprice = 0
        # 保存订单商品信息,查询数量
        for sku_id in sku_intid:
            try:
                goods = Goods.objects.get(pk=sku_id, is_delete=False, Goods_sku_Is_putaway=1)
            except Goods.DoesNotExist:
                return JsonResponse({"age": 10, "matter": '商品不存在'})

            # 获取购物车的数量
            try:
                count = cnn.hget(user_id, sku_id)
                count = int(count)
            except:
                return JsonResponse({"age": 11, "matter": '获取数量错误'})

            # 判断库存
            if goods.Goods_sku_Num < count:
                return JsonResponse({"age": 12, "matter": '商品数量不足'})

            # 保存再订单商品表
            try:
                OrdersGoods.objects.create(
                    OrderInformation=information,
                    goodsSku=goods,
                    goodsNum=count,
                    goodsPrice=goods.Goods_sku_Price,
                )
            except:
                return JsonResponse({"age": 13, "matter": '保存订单商品失败'})

            # 销量增加, 库存减少
            try:
                goods.Goods_sku_Sellnum += count
                goods.Goods_sku_Num -= count
                goods.save()
            except:
                return JsonResponse({"age": 14, "matter": '库存销量修改失败'})

            # 计算总价格
            allprice += count * goods.Goods_sku_Price

        # 计算商品总金额
        try:
            information.orderPrice = allprice
            information.save()
        except:
            return JsonResponse({"age": 15, "matter": '保存商品总金额失败'})

        # 删除rides的数据
        try:
            cnn.hdel(user_id, *sku_intid)
        except:
            return JsonResponse({"age": 16, "matter": '删除radis错误'})
        # 保存成功
        return JsonResponse({"age": 0, "matter": '保存商品信息成功', 'orderNum': number})
    else:
        return JsonResponse({"age": 0, "matter": '保存商品信息成功'})


# 订单详情
@old_request
def orderForm(request):
    return render(request, 'orderForm/allorder.html')
