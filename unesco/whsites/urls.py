from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',

    # ex: /sites/
    url(
        regex=r'^$',
        view=views.WHSiteListView.as_view(
            # paginate_by = '5' (https://djangosnippets.org/snippets/3023/)
            ),
        name='list'),

    # ex: /sites/NN/
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.WHSiteDetailView.as_view(),
        name='detail'),

    # ex: /sites/NN/json
    url(
        regex=r'^(?P<pk>\d+)/json/$',
        view=views.WHSiteDetailViewJSON.as_view(),
        name='data'),

    # a slug ex: /sites/abc/
    url(
        regex=r'^(?P<slug>\w+)/$',
        view=views.WHSiteDetailView.as_view(),
        name='slugdetail'),

    # ex: /sites/category/cultural/, /sites/state/uk/, /sites/region/europe/
    url(
        regex=r'^category/(?P<filter_value>\w+)/$',
        view=views.WHSiteListFilteredView.as_view(),
        name='bycategory'),

    # ex: /sites/category/cultural/, /sites/state/uk/, /sites/region/europe/
    url(
        regex=r'^state/(?P<filter_value>\w+)/$',
        view=views.WHSiteListFilteredView.as_view(),
        name='bystate'),

    # ex: /sites/category/cultural/, /sites/state/uk/, /sites/region/europe/
    url(
        regex=r'^region/(?P<filter_value>\w+)/$',
        view=views.WHSiteListFilteredView.as_view(),
        name='byregion'),

)
