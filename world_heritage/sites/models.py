from __future__ import unicode_literals

from django.db import models

# Create your models here.

# CRITERIA_CHOICES = ("i","ii","iii","iv","v","vi")

class Site(models.Model):
	owner = models.ForeignKey('auth.User', related_name='sites', on_delete=models.CASCADE)

	created = models.DateTimeField(auto_now_add=True)
	site = models.CharField(max_length=258,blank = False)
	criteria = models.CharField(max_length=100,blank=False)
	in_danger = models.BooleanField(default=False)
	http_url =  models.CharField(max_length=258,blank = False)
	image_url = models.CharField(max_length=258,blank = False)
	iso_code = models.CharField(max_length=128,blank = False)
	latitude = models.CharField(max_length=128,blank = False)
	longitude = models.CharField(max_length=128,blank = False)
	region = models.CharField(max_length=100,blank=False)
	short_description = models.CharField(max_length=2056,blank=False)
	states = models.CharField(max_length=512,blank=False)
	transboundary = models.CharField(max_length=128,blank=False)
	unique_number = models.CharField(max_length=128,blank=False)
	year = models.CharField(max_length=48,blank=False)

	cultural = models.BooleanField(default=False)
	natural = models.BooleanField(default=False)
	mixed = models.BooleanField(default=False)
	
	delisted = models.BooleanField(default=False)
