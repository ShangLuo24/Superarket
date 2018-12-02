from django.conf.urls import url
from orderForm.views import address, gladd, amendSite, deleteAlter, Alter, submit, notarize, orderForm, seve, pay, \
    pay_all

urlpatterns = [
    url(r'^address/$', address, name='添加地址'),
    url(r'^gladd/$', gladd, name='地址'),
    url(r'^amendSite/(?P<id>\d+)$', amendSite, name='修改地址'),
    url(r'^deleteAlter/$', deleteAlter, name='删除'),
    url(r'^Alter/$', Alter, name='修改'),
    url(r'^submit/$', submit, name='确认'),
    url(r'^seve/$', seve, name='保存'),
    url(r'^notarize/$', notarize, name='提交'),
    url(r'^orderForm/$', orderForm, name='订单中心'),
    url(r'^pay/$', pay, name='支付'),
    url(r'^pay_all/$', pay_all, name='支付结束'),
]
