from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from sites.models import Site

# Create your views here.
def index(request):
    sites = get_list_or_404(Site.objects)
    context = {'sites': sites}
    return render(request, 'sites/index.html', context)

def detail(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'sites/detail.html', {'site': site})

