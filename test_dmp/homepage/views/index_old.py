from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from django import forms
from lib.custform import CustomForm
from lib.custform import DataStoreForm

@view_function
def process_request(request):
	params = {}

	# handle the form
	form = DataStoreForm(request)
	if request.method == 'POST':
		form = DataStoreForm(request.POST)
		if form.is_valid():
			form.commit()
			#  Call a form.commit() from the customforms python script
			return HttpReponseRedirect('/homepage/account/')

	# render the response
	params['form'] = form
	return dmp_render_to_response(request, 'index.html', params)