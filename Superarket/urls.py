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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.cache import cache_page
from django.views.generic import RedirectView

from commodity.views import show

urlpatterns = [
    url(r'^$', cache_page(3600)(show)),  # 缓存到redis中首页
    url(r'^admin/', admin.site.urls),
    url(r'^search/', include('haystack.urls')),  # 全文搜索框架
    url(r'ckeditor', include("ckeditor_uploader.urls")),  # 用户上传的富文本域
    url(r'^user/', include('user.urls', namespace='user')),   # 用户模块
    url(r'^com/', include('commodity.urls', namespace='com')),   # 商品模块
    url(r'^car/', include('shoppingTrolley.urls', namespace='shop')),  # 购物车模块
    url(r'^add/', include('orderForm.urls', namespace='add')),  # 订单模块
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico'))
]
