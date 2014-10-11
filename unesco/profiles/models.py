from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class ProfileUser(AbstractUser):
    favourite_city = models.CharField(max_length=120, default="")
