# output the table
class Table(list):

	# subclasses should override the headings variable
	headers = ['Column 1', 'Column 2']
	fields = ['first_name', 'email']
	css_class = 'table table-bordered table-striped'
	rows_per_page = 5 

	def __init__(self, qry):
		self.qry = qry

	def paginate(self, request):
		try:
			page = int(request.REQUEST.get('table_page'))
		except ValueError:
			page = 0
		self.qry = self.qry[page * self.rows_per_page: (page + 1) * self.rows_per_page]

	def __str__(self):
		html = []
		html.append('<table class="{}">'.format(self.css_class))

		# print out the tr and th tags for the headers
		html.append('<tr>')
		for item in self.headers:
			# output each row for table headers
			html.append('<th>{}</th>'.format(item))
		html.append('</tr>')

		for obj in self.qry:
			# output each row
			html.append('<tr>')
			for field in self.fields:
				item = getattr(obj, field)
				html.append('<td>{}</td>'.format(item))
			html.append('</tr>')
		html.append('</table>')
		return ''.join(html)