from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # ex: /sites/
    url(
        regex = r'^$', 
        view = views.SiteListView.as_view(), 
        name='list'),

    # ex: /sites/5/
    url(
        regex = r'^(?P<pk>\d+)/$', 
        view = views.SiteDetailView.as_view(), 
        name='detail'),

)
