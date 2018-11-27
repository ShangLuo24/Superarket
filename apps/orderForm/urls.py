from django.conf.urls import url
from orderForm.views import address, gladd


urlpatterns = [
    url(r'^address/$', address, name='添加地址'),
    url(r'^gladd/$', gladd, name='地址'),
]
