from django.conf.urls import patterns, url

from sites import views

urlpatterns = patterns('',
    # ex: /sites/
    url(r'^$', views.index, name='index'),

    # ex: /sites/5/
    url(r'^(?P<site_id>\d+)/$', views.detail, name='detail'),
)
