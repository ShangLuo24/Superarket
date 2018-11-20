"""Superarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))s
"""
from django.conf.urls import url
from user.views import forget_password, reg, login, index, member, infor

urlpatterns = [
    url(r'^$', index, name='首页'),
    url(r'^login/$', login, name='登录'),
    url(r'^pass/$', forget_password, name='修改'),
    url(r'^reg/$', reg, name='注册'),
    url(r'^member/$', member, name='个人中心'),
    url(r'^infor/$', infor, name='个人信息'),
]
