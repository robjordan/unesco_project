from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',

    # ex: /visits/
    url(
        regex=r'^$',
        view=views.VisitListView.as_view(),
        name='list'),

    # ex: /visits/NN/
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.VisitDetailView.as_view(),
        name='detail'),

    # ex: /visits/create/
    url(
        regex=r'^create/$',
        view=views.VisitCreateView.as_view(),
        name='create'),

)
