from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import *
from django.contrib.gis.measure import D
from datetime import datetime


# Create your models here.
class State(models.Model):
    # attributes
    name = models.CharField(max_length=120, default="")
    iso_code = models.CharField(max_length=120, default="")
    # methods

    def __str__(self):
        return self.name


class Region(models.Model):
    # attributes
    name = models.CharField(max_length=120, default="")
    # methods

    def __str__(self):
        return self.name


class Category(models.Model):
    # attributes
    name = models.CharField(max_length=20, default="")
    # methods

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class WHSite(models.Model):
    # attributes
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, default="")
    id_number = models.PositiveSmallIntegerField(
        "ID number", null=True, blank=False)
    short_description = models.TextField(
        blank=True, max_length=4000, default="")
    justification = models.TextField(blank=True, max_length=4000, default="")
    http_url = models.URLField("URL", blank=True, default="")
    image_url = models.URLField("Image URL", blank=True, default="")
    inscribed_date = models.PositiveSmallIntegerField(
        'inscribed date', null=True, blank=True)
    latitude = models.FloatField('latitude', null=True, blank=True)
    longitude = models.FloatField('longitude', null=True, blank=True)
    map_point = geomodels.PointField(blank=True, null=True)
    globe_point = geomodels.PointField(geography=True, blank=True, null=True)
    states = models.ManyToManyField(State, null=True)
    region = models.ForeignKey(Region, null=True)
    category = models.ForeignKey(Category, null=True)
    objects = geomodels.GeoManager()
    # methods

    def save(self):
        if self.latitude is not None:
            lString = 'POINT({} {})'.format(self.longitude, self.latitude)
            self.map_point = fromstr(lString)
            self.globe_point = fromstr(lString)
        self.last_modified = datetime.now()
        super(WHSite, self).save()

    def nearby_sites(self, d=100000):
        # exclude self
        n = [s for s in WHSite.objects.filter(
            globe_point__distance_lt=(self.globe_point, d)) if s.pk != self.pk]
        return n

    def as_geojson(self):
        coords = [self.longitude, self.latitude]
        geojson = {"type": "Feature", "geometry": {
            "type": "Point", "coordinates": coords
        }, "properties": {"name": self.name}}
        return geojson

    def states_list(self):
        return ", ".join(map(str, self.states.all()))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "UNESCO Site"


class Visit(models.Model):
    # attributes
    site = models.ForeignKey(WHSite, null=False)
    visitor = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
    date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True, max_length=4000, default="")
    # methods

    def __str__(self):
        return str(
            self.visitor
            )+" visited "+str(self.site)+" on "+str(self.date)
