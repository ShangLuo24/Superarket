from django.conf.urls import url
from orderForm.views import address, gladd, amendSite, deleteAlter, Alter

urlpatterns = [
    url(r'^address/$', address, name='添加地址'),
    url(r'^gladd/$', gladd, name='地址'),
    url(r'^amendSite/(?P<id>\d+)$', amendSite, name='修改地址'),
    url(r'^deleteAlter/$', deleteAlter, name='删除'),
    url(r'^Alter/$', Alter, name='修改'),
]
