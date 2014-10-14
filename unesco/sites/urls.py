from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # ex: /sites/
    url(
        regex = r'^$', 
        view = views.SiteListView.as_view(), 
        name='list'),

    # ex: /sites/NN/
    url(
        regex = r'^(?P<pk>\d+)/$', 
        view = views.SiteDetailView.as_view(), 
        name='detail'),

    # ex: /sites/abc/
    url(
        regex = r'^(?P<slug>\w+)/$', 
        view = views.SiteDetailView.as_view(), 
        name='detail'),

)
