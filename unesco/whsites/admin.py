from django.contrib import admin

# Register your models here.
from whsites.models import WHSite
from whsites.models import State
from whsites.models import Region
from whsites.models import Category
from whsites.models import Visit


class WHSiteAdmin(admin.ModelAdmin):
    fields = ['name', 'slug', 'id_number', 'short_description',
              'justification', 'http_url', 'image_url',
              'inscribed_date', 'longitude', 'latitude', 'map_point',
              'globe_point', 'states', 'region', 'category']
    list_filter = ['states']
    list_display = ['name']
    search_fields = ['name']
    filter_vertical = ['states']
    ordering = ['name']


class StateAdmin(admin.ModelAdmin):
    ordering = ['name']


class VisitAdmin(admin.ModelAdmin):
    ordering = ['date']

admin.site.register(WHSite, WHSiteAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Region)
admin.site.register(Category)
