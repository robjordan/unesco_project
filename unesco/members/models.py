from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from registration.models import RegistrationManager
# import the logging library
import logging
from django.core.exceptions import ObjectDoesNotExist
from visits.models import Visit

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='member', unique=True)
    favourite_city = models.CharField(max_length=120, default="")
    social_response = models.TextField(null=True, blank=True)

    def visits(self):
        return Visit.objects.filter(visitor=self.user)

    def __str__(self):
        return self.user.username


def create_member_from_social_profile(
        backend, user, response, *args, **kwargs
):
    try:
        profile = user.member
    except ObjectDoesNotExist:
        profile = Member(user=user)
        profile.save()
    profile.social_response = str(response)
    profile.save()
    return {'profile': profile}
