from django.conf.urls import url, include

from commodity.views import show, category, detail

urlpatterns = [
    url(r'^show/$', show, name='首页'),
    url(r'^category/(?P<id>\d+)/(?P<order>\d+)/$', category, name='商店'),
    url(r'^detail/(?P<id>\d+)/$', detail, name='详情'),
]
