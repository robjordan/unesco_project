from django.contrib import admin

# Register your models here.
from profiles.models import ProfileUser, Profile

class ProfileUserAdmin(admin.ModelAdmin):
    fields = ['email', 'is_superuser', 'is_staff', 'is_active', 'name',]
    

class ProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'favourite_city']
    list_display = ['user']

admin.site.register(ProfileUser, ProfileUserAdmin)
admin.site.register(Profile, ProfileAdmin)


