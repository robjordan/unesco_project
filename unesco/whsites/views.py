from django.views.generic import ListView, DetailView, TemplateView
# from django.views.generic import TemplateView, RedirectView, CreateView
# from django.views.generic import UpdateView, DeleteView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import HttpResponse, Http404
from .models import WHSite
from .models import State
from .models import Region
from .models import Category
# from .forms import WHSiteFilterForm
from braces.views import JSONResponseMixin, AjaxResponseMixin


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
#        context['latest_articles'] = Article.objects.all()[:5]
        return context


class WHSiteListView(ListView):
    model = WHSite


class WHSiteListFilteredView(ListView):

    def get_queryset(self):

        path = self.request.path.split("/")
        self.category = []
        self.region = []
        self.states = []

        if path[2] == 'category':
            self.category = get_object_or_404(Category, pk=path[3])
            return WHSite.objects.filter(category=self.category)
        elif path[2] == 'region':
            self.region = get_object_or_404(Region, pk=path[3])
            return WHSite.objects.filter(region=path[3])
        elif path[2] == 'state':
            self.states = State.objects.filter(iso_code=path[3])
            if not self.states:
                raise Http404('No state matches the given query.')
            return WHSite.objects.filter(states__contains=self.states)

    def get_context_data(self, **kwargs):
        # import pdb; pdb.set_trace()
        # Call the base implementation first to get a context
        context = super(
            WHSiteListFilteredView, self).get_context_data(**kwargs)
        # Construct a search criteria string
        context['criteria'] = ""

        if self.category:
            context['criteria'] += "Category: " + str(self.category)
        if self.region:
            context['criteria'] += "Region: " + str(self.region)
        if self.states:
            context['criteria'] += "State: "
            for s in self.states:
                context['criteria'] += str(s) + " "
        return context


# Original
class WHSiteDetailView(DetailView):
    model = WHSite


class WHSiteDetailViewJSON(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = WHSite
    json_dumps_kwargs = {"indent": 2}

    def get(self, request, *args, **kwargs):
        return self.render_json_response(self.get_object().as_geojson())


class WHSiteDetailViewAJAX(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = WHSite
    json_dumps_kwargs = {"indent": 2}

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_object())



# The following is abandoned attempt at a facet-filtered view:
# it depends on custom template tags... too hard right now
#
# def whsite_list(request):
#     qs = WHSite.objects.order_by('name')
#
#     form = WHSiteFilterForm(data=request.REQUEST)
#
#     facets = {
#         'selected': {},
#         'categories': {
#             'states': State.objects.all(),
#             'regions': Region.objects.all(),
#             'categories': Category.objects.all(),
#         },
#     }
#
#     if form.is_valid():
#         state = form.cleaned_data['state']
#         if state:
#             facets['selected']['state'] = state
#             qs = qs.filter(state=state).distinct()
#
#         region = form.cleaned_data['region']
#         if region:
#             facets['selected']['region'] = region
#             qs = qs.filter(region=region).distinct()
#
#         state = form.cleaned_data['state']
#         if state:
#             facets['selected']['state'] = state
#             qs = qs.filter(state=state).distinct()
#
#         context = {
#             'form': form,
#             'facets': facets,
#             'object_list': qs,
#             }
#         return render(request, "whsites/whsite_filtered_list.html", context)
