from django.conf.urls import include, patterns, url
from django.contrib import admin
# from account import *

urlpatterns = patterns('', 
    url(r'^sites/', include('sites.urls', namespace='sites', app_name='sites')),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
