from django.views.generic import ListView, DetailView
# from django.views.generic import TemplateView, RedirectView, CreateView, UpdateView, DeleteView
from .models import WHSite


# Create your views here.
class WHSiteListView(ListView):
    model = WHSite

class WHSiteDetailView(DetailView):
    model = WHSite


