from django.conf.urls import include, patterns, url
from django.contrib import admin
from members.forms import MemberRegistrationForm
from registration.backends.default.views import RegistrationView
from django.views.generic.base import RedirectView

urlpatterns = patterns('', 
    url(r'^sites/', include('whsites.urls', namespace='whsites', app_name='whsites')),

    # the following are locally-defined based on djang.contrib.auth
    url(r'^members/', include('members.urls', namespace='members', app_name='members')),
    url(r'^admin/', include(admin.site.urls)),

    # this ensures that member profile gets registered when a user gets registered
    url(r'members/register/$', RegistrationView.as_view(form_class = MemberRegistrationForm, template_name='members/member_form.html'), name = 'register'),

    # following are from django-registration plugin
    url(r'^members/', include('registration.backends.default.urls')),

    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'))
)

