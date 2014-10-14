from django.views.generic import ListView, DetailView, UpdateView, CreateView
# from django.views.generic import TemplateView, RedirectView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from braces.views import LoginRequiredMixin
from .models import ProfileUser


# Create your views here.
class ProfileUserListView(LoginRequiredMixin, ListView):
    model = ProfileUser

class ProfileUserDetailView(LoginRequiredMixin, DetailView):
    model = ProfileUser

class ProfileUserUpdateView(LoginRequiredMixin, UpdateView):
    model = ProfileUser

@login_required
def home(request):
    return HttpResponseRedirect(
        reverse("profiles:detail", kwargs={"pk": request.user.pk}))

class ProfileUserCreateView(CreateView):
    model = ProfileUser
#    fields = ['email', 'name']

#    def get(self, request, *args, **kwargs):
#        return HttpResponse("ProfileUserCreate")
#    fields = ('username', 'email', 'password', 'favourite_city')
    success_url = '/profiles/home'

    
