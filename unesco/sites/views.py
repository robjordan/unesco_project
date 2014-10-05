#from django.shortcuts import render, get_object_or_404, get_list_or_404
#from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Site

# Create your views here.
class SiteListView(ListView):
    model = Site

class SiteDetailView(DetailView):
    model = Site


