from django.conf.urls import patterns, url
from authtools import views
from . import views

urlpatterns = patterns('',
    # ex: /profiles/
    url(
        regex = r'^$', 
        view = views.ProfileUserListView.as_view(), 
        name='list'),

    # ex: /profiles/5/
    url(
        regex = r'^(?P<pk>\d+)/$', 
        view = views.ProfileUserDetailView.as_view(), 
        name='detail'),

    # ex: /profiles/home/
    url(
        regex = r'^home/$',
        view = 'profiles.views.home',
        name = 'home'),

    # ex: /profiles/create
    url(
        regex = r'^create/$',
        view = views.ProfileUserCreateView.as_view(),
        name = 'create'),

    url(r'^login/$', 'authtools.views.login', name='login'),
    url(r'^logout/$', 'authtools.views.logout', name='logout'),
    url(r'^password_change/$', 'authtools.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'authtools.views.password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'authtools.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'authtools.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/done/$', 'authtools.views.password_reset_complete', name='password_reset_complete'),


)
