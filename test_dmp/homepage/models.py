from django.db import models
from django.conf import settings  
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime, os, sys

class Image(models.Model):
	'''
	This is a model class that stores all of my models
	'''
	title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
	date_created = models.DateTimeField(default=datetime.datetime.now)
	imageSource = models.CharField(max_length=200)

	def __unicode__(self):
	    return self.title

class User(models.Model):
	first_name = models.TextField(blank=True, null=True)
	email = models.TextField(blank=True, null=True)