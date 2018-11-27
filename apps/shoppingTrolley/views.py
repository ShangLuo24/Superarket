from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django_redis import get_redis_connection

from commodity.models import Goods
from user.helper import old_request

"""
# 类型转换
def to_int(str):
    try:
        int(str)
        return int(str)
    except ValueError:  # 报类型错误，说明不是整型的
        try:
            float(str)  # 用这个来验证，是不是浮点字符串
            return int(float(str))
        except ValueError:  # 如果报错，说明即不是浮点，也不是int字符串。   是一个真正的字符串
            return False
# 导入redis连接方法
from django_redis import get_redis_connection
# 使用默认配置连接到redis
cnn = get_redis_connection('default')
# 使用连接上的方法操作redis
cnn.hset('对象名'，'属性' ，'值')
"""


# 商品详情页面添加商品
def shopping(request):
    # 获取用户id,验证是否登录
    user_id = request.session.get("user_id")
    # print(user_id)
    if user_id is None:
        return JsonResponse({'age': 0, 'clue': '用户尚未登录'})

    # 获取商品id 获取商品数量
    number = request.POST.get('number')
    sku_id = request.POST.get('sku_id')

    # 获取商品数量
    try:
        number = int(number)
    except:
        return JsonResponse({'age': 1, 'clue': '数量未选择'})
    if number > Goods.Goods_sku_Num:
        return JsonResponse({'age': 4, 'clue': '库存不足'})

    # 获取商品id
    try:
        sku_id = int(sku_id)
        Goods.objects.get(pk=sku_id)
    except Exception:
        return JsonResponse({'age': 2, 'clue': '商品不存在'})

    # 保存到数据库中, 设置
    user_id = "User_{}".format(user_id)
    cnn = get_redis_connection('default')
    cnn.hincrby(user_id, sku_id, number)
    return JsonResponse({'age': 3, 'clue': '添加购物车成功'})


# 商品分类页面添加商品
def showshopp(request):
    # 获取用户信息
    user_id = request.session.get("user_id")
    # print(user_id)
    if user_id is None:
        return JsonResponse({'age': 0, 'clue': '用户尚未登录'})

    # 获取商品id
    sku_id = request.POST.get('sku_id')

    # 设置商品数量
    number = request.POST.get('number')

    # 保存到数据库中, 设置
    user_id = "User_{}".format(user_id)
    cnn = get_redis_connection('default')
    cnn.hincrby(user_id, sku_id, number)

    # 判断数量是否为零
    new_num = cnn.hget(user_id, sku_id)
    if int(new_num) == 0:
        cnn.hdel(user_id, sku_id)

    # 获取商品总数
    all_num = cnn.hvals(user_id)
    start = 0
    for an in all_num:
        print(int(an))
        start += int(an)
    print(start)
    return JsonResponse({'age': 1, "all_num": start})


@old_request
def shopper(request):
    # 查询用户id
    user_id = request.session.get("user_id")
    user_id = "User_{}".format(user_id)
    # 建立连接
    cnn = get_redis_connection('default')
    # 获取商品信息
    # 获取数量
    over = cnn.hgetall(user_id)
    # print(over)
    # print(over)
    apple = over.items()
    # print(apple)
    list = []
    a = 0
    for key, value in apple:
        apple = Goods.objects.get(pk=key)
        price = apple.Goods_sku_Price
        a += (int(price) * int(value))
        apple.count = value
        list.append(apple)
    print(a)
    context = {
        "goods": list,
        "price": a,
    }
    return render(request, "shopping_trolley/shopcart.html", context)
