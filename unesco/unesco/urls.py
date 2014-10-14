from django.conf.urls import include, patterns, url
from django.contrib import admin

urlpatterns = patterns('', 
    url(r'^sites/', include('sites.urls', namespace='sites', app_name='sites')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles', app_name='profiles')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^login/$', "django.contrib.auth.views.login", 
#        {"template_name": "login.html"}, name="login"),
#    url(r'^logout/$', "django.contrib.auth.views.logout_then_login", 
#        name="logout"),
#    url(r'^accounts/', include('authtools.urls', namespace='authtools', app_name='authtools')),
)

