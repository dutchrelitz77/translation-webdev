from django.conf import settings
from django_mako_plus.controller import view_function
from datetime import datetime
from .. import dmp_render, dmp_render_to_response
from django import forms
from lib.table_output import Table
from homepage import models as hmod


@view_function
def process_request(request):
	template_vars = {}

	template_vars['initial_page'] = 5
	return dmp_render_to_response(request, 'tabledemo.html', template_vars)

@view_function
def get_table(request):
	template_vars = {}

	users = UserTable(hmod.User.objects.all())
	users.paginate(request)

	# Specify the table as the renderer
	template_vars['table'] = users
	return dmp_render_to_response(request, 'tabledemo.get_table.html', template_vars)


class UserTable(Table):
	headers = ['First Name', 'Email']
	fields = ['first_name', 'email']