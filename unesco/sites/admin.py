from django.contrib import admin

# Register your models here.
from sites.models import Site
from sites.models import State

class SiteAdmin(admin.ModelAdmin):
    fields = ['name', 'inscribed_date', 'longitude', 'latitude', 'state']
    list_filter = ['state']
    list_display = ['name', 'state']
    search_fields = ['name']

admin.site.register(Site, SiteAdmin)
admin.site.register(State)

