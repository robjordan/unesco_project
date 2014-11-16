from django.views.generic import ListView, DetailView, UpdateView, CreateView
# from django.views.generic import TemplateView, RedirectView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from braces.views import LoginRequiredMixin, UserPassesTestMixin, SuperuserRequiredMixin
from django.http import HttpResponseRedirect
from .models import Member


# Only the member in question or a superuser can view member profiles
class OwnerOrSuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self, user):
        requestor = self.request.user.member.pk
        owner = self.get_object().pk
        if not (user.is_superuser or requestor == owner):
            raise PermissionDenied
        else:
            return True

# Create your views here.
class MemberListView(LoginRequiredMixin, SuperuserRequiredMixin, ListView):
    model = Member

class MemberDetailView(LoginRequiredMixin, OwnerOrSuperuserRequiredMixin, DetailView):
    model = Member

class MemberUpdateView(LoginRequiredMixin, OwnerOrSuperuserRequiredMixin, UpdateView):
    model = Member

@login_required
def home(request):
    return HttpResponseRedirect(
        reverse("members:detail", kwargs={"pk": request.user.member.pk}))

class MemberCreateView(CreateView):
    model = Member
    success_url = reverse_lazy("members:home")

