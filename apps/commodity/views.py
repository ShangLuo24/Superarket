from django.shortcuts import render, redirect

from commodity.models import SlideShow, Home, Activity, Division, Goods, Class


def show(request):
    """
    首页
    :param request:
    :return:
    """
    # 轮转图
    Slide = SlideShow.objects.filter(is_delete=False).order_by('-Page_Order')
    # 不规则展示区
    home = Home.objects.filter(is_delete=False)
    # 特色专区
    act = Activity.objects.filter(is_delete=False).order_by('-Activity_Order')
    # for a in act:
    #     oppo = a.division_set.all()
    #     for o in oppo:
    #         print(o.Division_sku.Goods_spu_id.Goods_spu_name)
    #         print(o.Division_sku.Goods_sku_name)
    #         print(o.Division_sku.Goods_sku_Unitinfo)
    #         print(o.Division_sku_id)
    #         print(111111111111111111111111111)
    context = {
        'data': Slide,
        'home': home,
        'activ': act,
    }
    return render(request, 'show/index.html', context)


def category(request, id, order):
    """
    商品页
    :param request:
    :return:
    """
    # 查询商品分类列表
    clas = Class.objects.filter(is_delete=False)
    # 查询商品分类的商品信息
    good = Goods.objects.filter(is_delete=False, Goods_sku_Is_putaway=1, Goods_sku_cate_id_id=id)

    # 类型转换
    try:
        id = int(id)
        order = int(order)
    except:
        return redirect("com:首页")

    # 优化,增加条件查询
    # 设置order排序条件
    if order == 0:
        good = good
    elif order == 1:
        good = good.order_by("-Goods_sku_Sellnum")
    elif order == 2:
        good = good.order_by("-Goods_sku_Price")
    elif order == 3:
        good = good.order_by("Goods_sku_Price")
    elif order == 4:
        good = good.order_by("-create_time")

    # 默认查询第一个商品列表
    if id == 0:
        good = good.first()
        id = good.pk

    context = {
        'id': id,
        'clas': clas,
        'Good': good,
        'order': order,
    }
    return render(request, 'show/category.html', context)


def detail(request, id):
    """
    详情页面
    :param request:Create create
    :return:
    """
    try:
        sku = Goods.objects.get(pk=id, is_delete=False)
    except Goods.DoesNotExist:
        return redirect('com:首页')
    context = {
        'sku': sku,
    }
    return render(request, 'show/detail.html', context)
