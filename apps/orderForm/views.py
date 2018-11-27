from django.shortcuts import render
from django.http import HttpResponse


def address(request):
    """
    添加收货地址
    :param request:
    :return:
    """
    return render(request, "orderForm/address.html")


def gladd(requset):
    """
    收货地址展示页
    :param requset:
    :return:
    """
    return render(requset, "orderForm/gladdress.html")
