from django.db import models
from django.conf import settings
from authtools.models import AbstractNamedUser

# Create your models here.
class ProfileUser(AbstractNamedUser):
    full_name = models.CharField('full name', max_length=255, blank=True)

    # methods
    def __str__(self):
        return self.name
    def get_full_name(self):
        return self.full_name

    class Meta:
        verbose_name = "User"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    favourite_city = models.CharField(max_length=120, default="")
