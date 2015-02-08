from django.contrib import admin
from visits.models import Visit


# Register your models here.
class VisitAdmin(admin.ModelAdmin):
    ordering = ['date']

admin.site.register(Visit, VisitAdmin)
