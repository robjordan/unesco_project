from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import WHSite


# Create your views here.
class SiteListView(ListView):
    model = WHSite

class SiteDetailView(DetailView):
    model = WHSite


