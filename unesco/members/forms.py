from registration.forms import RegistrationForm
from registration.signals import user_registered
from django import forms
from .models import Member

class MemberRegistrationForm(RegistrationForm):
    favourite_city = forms.CharField(max_length=120, label = "Favourite city:")

def user_registered_callback(sender, user, request, **kwargs):
    profile = Member(user = user)
    profile.favourite_city = request.POST["favourite_city"]
    profile.save()
 
user_registered.connect(user_registered_callback)
