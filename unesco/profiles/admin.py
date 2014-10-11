from django.contrib import admin

# Register your models here.
from profiles.models import ProfileUser

class ProfileUserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'last_login', 'date_joined', 'favourite_city']
    ordering = ['last_name']

admin.site.register(ProfileUser, ProfileUserAdmin)


