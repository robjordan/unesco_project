from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^sites/', include('sites.urls', namespace='sites', app_name='sites')),
    url(r'^admin/', include(admin.site.urls)),
)
