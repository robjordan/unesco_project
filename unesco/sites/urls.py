from django.conf.urls import patterns, url

from sites import views

urlpatterns = patterns('',
    # ex: /sites/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # ex: /sites/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
