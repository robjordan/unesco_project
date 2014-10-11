from django.conf.urls import patterns, url

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

)
