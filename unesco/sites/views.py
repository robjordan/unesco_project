from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from sites.models import Site

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'sites/index.html'
    
    def get_queryset(self):
        """Return all sites."""
        return Site.objects.order_by('region')

class DetailView(generic.DetailView):
    model = Site
    template_name = 'sites/detail.html'


