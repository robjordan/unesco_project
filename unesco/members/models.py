from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from registration.models import RegistrationManager
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='member', unique=True)
    favourite_city = models.CharField(max_length=120, default="")

    def __str__(self):
        return self.user.username
