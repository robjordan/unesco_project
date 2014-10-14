from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^sites/', include('sites.urls', namespace='sites', app_name='sites')),
    url(r'^members/', include('members.urls', namespace='members', app_name='members')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^accounts/', include('registration.backends.default.urls')),
)

