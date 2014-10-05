from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, UpdateView
from .models import Site

# Create your views here.
class SiteListView(ListView):
    model = Site

class SiteDetailView(DetailView):
    model = Site


