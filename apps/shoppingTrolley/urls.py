from django.conf.urls import url, include
from django.contrib import admin

from shoppingTrolley.views import shopping

urlpatterns = [
    url(r'^shop/$', shopping, name='购物车')
]
