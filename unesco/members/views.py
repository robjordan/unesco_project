from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
# from django.views.generic import TemplateView, RedirectView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from .models import Member

# Create your views here.
class MemberListView(LoginRequiredMixin, ListView):
    model = Member

class MemberDetailView(LoginRequiredMixin, DetailView):
    model = Member

class MemberUpdateView(LoginRequiredMixin, UpdateView):
    model = Member

@login_required
def home(request):
    return HttpResponseRedirect(
        reverse("members:detail", kwargs={"pk": request.user.member.pk}))

class MemberCreateView(CreateView):
    model = Member
    success_url = reverse_lazy("members:home")
