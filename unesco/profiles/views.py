from django.views.generic import ListView, DetailView, UpdateView
# from django.views.generic import TemplateView, RedirectView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import ProfileUser


# Create your views here.
class ProfileUserListView(ListView):
    model = ProfileUser

class ProfileUserDetailView(DetailView):
    model = ProfileUser

class ProfileUserUpdateView(UpdateView):
    model = ProfileUser

@login_required
def home(request):
    return HttpResponseRedirect(
        reverse("profiles:detail", kwargs={"pk": request.user.pk}))
