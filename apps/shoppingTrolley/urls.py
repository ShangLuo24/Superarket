from django.conf.urls import url, include
from django.contrib import admin

from shoppingTrolley.views import shopping, shopper, showshopp

urlpatterns = [
    url(r'^shop/$', shopping, name='购物'),
    url(r'^shopper/$', shopper, name='购物车'),
    url(r'showshopp/$', showshopp, name='商品页add'),
]
