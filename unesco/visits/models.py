from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django_date_extensions.fields import ApproximateDateField
from whsites.models import WHSite


# Create your models here.
class Visit(models.Model):
    # attributes
    site = models.ForeignKey(WHSite, null=False)
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
#    date = models.DateField(null=True, blank=True)
    date = ApproximateDateField(null=False, blank=False)
    comments = models.TextField(blank=True, max_length=4000, default="")
    # methods

    def get_absolute_url(self):
        return reverse("visits:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(
            self.date)+": "+str(self.visitor)+" visited "+str(self.site)
