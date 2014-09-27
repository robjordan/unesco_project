from django.contrib import admin

# Register your models here.
from sites.models import Site
from sites.models import State
from sites.models import Region
from sites.models import Category

class SiteAdmin(admin.ModelAdmin):
    fields = ['name', 'id_number', 'short_description', 'justification', 'http_url', 'image_url', 'inscribed_date', 'longitude', 'latitude', 'states', 'region', 'category']
    list_filter = ['states']
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Site, SiteAdmin)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Category)

