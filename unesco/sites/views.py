from django.shortcuts import render
from django.http import HttpResponse
from sites.models import Site

# Create your views here.
def index(request):
    output = "<ul>"
    recent_sites = Site.objects.order_by('-inscribed_date')
    for s in recent_sites:
        output = output + "<li>" + str(s.inscribed_date) + ": " + "<a href=" + str(s.pk) + ">" + s.name + "</a>; " + str(s.state) + "</li>"
    output = output + "</ul>"
    return HttpResponse(output)

def detail(request, site_id):
    return HttpResponse(Site.objects.get(pk=site_id))

