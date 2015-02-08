from django import forms
from django.forms import ModelForm
from visits.models import Visit


class VisitForm(ModelForm):

    class Meta:
        model = Visit
        fields = '__all__'
