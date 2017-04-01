from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'^(?P<pk>.*)/$', views.mineral_list, name='list'),
    url(r'^random', views.mineral_random, name='random'),
    url(r'^', views.mineral_list, name='list'),
]
