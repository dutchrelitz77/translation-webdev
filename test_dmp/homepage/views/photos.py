from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from django import forms
from lib.custform import CustomForm
from lib.custform import DataStoreForm
from homepage import models

@view_function
def process_request(request):
	params = {}
	images = models.Image.objects.all()

	# render the response
	params['images'] = images
	return dmp_render_to_response(request, 'photos.html', params)