# Create a custom widget here
import django.forms

class DateDropDownInput(django.forms.DateInput):
	# do some custom widget code here
	def __init__(self, *args, **kwargs):
		kwargs['format'] = '%Y-%m-%d'
		super().__init__(*args, **kwargs)

	def render(self, name, value, attrs=None):
		return super().render(name, value, attrs)+('''
			<span id = '%s'></span>
		''' % name) + ('''
			<script>
				$(function() {
					var input = $('#%s').siblings('input[name="%s"]');
					input.datetimepicker({
						mask: '1997-11-39',
						timepicker: false,
						format: 'Y-m-d',
						allowblank: true,
					}); //datepicker
				});
			</script>

		''' % (name, name))