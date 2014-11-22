from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # ex: /sites/
    url(
        regex = r'^$', 
        view = views.WHSiteListView.as_view(), 
        name='list'),

    # ex: /sites/NN/
    url(
        regex = r'^(?P<pk>\d+)/$', 
        view = views.WHSiteDetailView.as_view(), 
        name='detail'),

    # a slug ex: /sites/abc/
    url(
        regex = r'^(?P<slug>\w+)/$', 
        view = views.WHSiteDetailView.as_view(), 
        name='detail'),

    # ex: /sites/category/cultural/, /sites/state/uk/, /sites/region/europe/
    url(
        regex = r'^(?P<filter_kw>\w+)/(?P<filter_value>\w+)/$', 
        view = views.WHSiteListFilteredView.as_view(), 
        name='list'),

)
