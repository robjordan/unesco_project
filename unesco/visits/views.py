from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView
# from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from django.shortcuts import get_list_or_404
# from django.http import HttpResponse, Http404
from braces.views import LoginRequiredMixin
from .models import Visit


# Copied this from 2 Scoops of Django: p.111
class VisitActionMixin(object):
    fields = ('site', 'date', 'comments')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        form.instance.visitor = self.request.user
        return super(VisitActionMixin, self).form_valid(form)


class VisitListView(ListView):
    model = Visit


class VisitDetailView(DetailView):
    model = Visit


class VisitCreateView(LoginRequiredMixin, VisitActionMixin, CreateView):
    model = Visit
    success_msg = "Visit recorded"

    def get_initial(self):
        initial = super(VisitCreateView, self).get_initial()
        try:
            initial.update({'site': self.request.GET['site']})
        except KeyError:
            pass
        return initial

    def get_success_url(self):
        url = super(VisitCreateView, self).get_success_url()
        try:
            url = self.request.GET['success_url']
        except KeyError:
            pass
        return url


class VisitUpdateView(LoginRequiredMixin, VisitActionMixin, UpdateView):
    model = Visit
    success_msg = "Visit updated"
