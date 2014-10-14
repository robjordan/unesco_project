from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # /members/
    url(regex=r'^$', view=views.MemberListView.as_view(), name='list'),
    # /members/<numeric>/
    url(regex=r'^(?P<pk>\d+)/$', view=views.MemberDetailView.as_view(), name='detail'),
    # /members/home/
    url(r'^home/$', view=views.home, name='home'),
    # /members/create/
    url(r'^create/$', views.MemberCreateView.as_view(), name='create'),
    # /members/login/
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # /members/logout/
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # /members/password_change/
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', kwargs={'post_change_redirect': 'members:password_change_done'}, name='password_change'),
    # /members/password_change/done/
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    # /members/password_reset/
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', kwargs={'post_reset_redirect': 'members:password_reset_done'}, name='password_reset'),
    # /members/password_reset/done/
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # /members/reset/<uid>/
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    # /members/reset/done/
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)
