from django.db import models
from django.conf import settings

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
	id_number = models.PositiveSmallIntegerField("ID number", null=True, blank=False)
	short_description = models.TextField(blank=True, max_length=4000, default="")
	justification = models.TextField(blank=True, max_length=4000, default="")
	http_url = models.URLField("URL", blank=True, default="")
	image_url = models.URLField("Image URL", blank=True, default="")
	inscribed_date = models.PositiveSmallIntegerField('inscribed date', null=True, blank=True)
	latitude = models.FloatField('latitude', null=True, blank=True)
	longitude = models.FloatField('longitude', null=True, blank=True)
	states = models.ManyToManyField(State, null=True)
	region = models.ForeignKey(Region, null=True)
	category = models.ForeignKey(Category, null=True)
	# methods
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Site"

class Visit(models.Model):
	# attributes
	site = models.ForeignKey(WHSite, null=False)
	visitor = models.ForeignKey(settings.AUTH_USER_MODEL, null=False)
	date = models.DateField(null=True, blank=True)
	comments = models.TextField(blank=True, max_length=4000, default="")
	# methods
	def __str__(self):
		return str(str(self.visitor) + " visited " + str(self.site) + " on " + str(self.date))
