from django.conf import settings
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django import forms
from lib.custform import CustomForm
from lib.custform import DataStoreForm
from django.http import HttpResponse
from homepage import models as hmod
import os.path
from lib.uploadWidget import FileUploader

# function to upload files
def handle_uploaded_file(file_request_object, file_path):
    with open(file_path, 'wb+') as destination:
        for chunk in file_request_object.chunks():
            destination.write(chunk)

@view_function
def process_request(request):
	template_vars = {}

	form = UploaderForm()
	if request.method == 'POST':
		form = UploaderForm(request.POST)
		if form.is_valid():
			print('>>>>> main form', form.cleaned_data['upload_fullname'])
			form = UploaderForm()

	template_vars['form'] = form
	return dmp_render_to_response(request, 'uploader.html', template_vars)

class UploaderForm(forms.Form):
	name = forms.CharField()
	upload_fullname = forms.CharField(widget=forms.HiddenInput)
	upload_file = forms.FileField(required=False, widget=FileUploader)

@view_function
def upload(request):
	# take request.FILES and save the bytes to disk somewhere
	filename = request.FILES['upload'].name
	fullname = os.path.join('homepage/media/files', filename)

	# use function to upload file
	handle_uploaded_file(request.FILES['upload'], fullname)

	# return
	return HttpResponse(filename)