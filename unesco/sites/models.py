from django.db import models


# Create your models here.
class State(models.Model):
	# attributes
	name = models.CharField(max_length=120)
	# methods
	def __str__(self):
		return self.name

class Site(models.Model):
	# attributes
	name = models.CharField(max_length=200)
	inscribed_date = models.PositiveSmallIntegerField('inscribed date')
	latitude = models.FloatField('latitude')
	longitude = models.FloatField('longitude')
	state = models.ForeignKey(State)
	# methods
	def __str__(self):
		return self.name
