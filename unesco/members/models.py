from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='member')
    favourite_city = models.CharField(max_length=120, default="")
