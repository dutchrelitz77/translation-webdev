import django.forms as forms
from lib.widgets import DateDropDownInput


class CustomForm(forms.Form):
    """
    Base form to be used by all forms
    """
    form_id = 'form'
    form_action = None
    #submit_buttons = [ forms.SubmitButton('Submit', css_class="btn btn-primary") ]
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        # call the superclass
        super().__init__(*args, **kwargs)
        # call the init method
        self.init()

    def init(self):
        # define fields here
        pass

    def commit(self):
        pass

    def as_full(self):
        #prints the form
        pass
    
class DataStoreForm(CustomForm):
    """
    Form for adding a data store
    """
    def init(self):
        # define fields here
        self.fields['data_store_name-%s' % self.request.get_webid()] = forms.CharField(label="Data Store Name:", widget=forms.TextInput(attrs={'class' : 'form-control'}))
        self.fields['data_store_type-%s' % self.request.get_webid()] = forms.ChoiceField(label="Data Store Type:",
                                                                                                choices=(('1',1), ('2',2), ('3',3), ('4',4)),
                                                                                                widget = forms.RadioSelect(attrs={'class': 'radio-inline'})) # Fix this portion
        self.fields['data_store_endpoint-%s' % self.request.get_webid()] = forms.CharField(label="Data Endpoint:", widget=forms.TextInput(attrs={'class' : 'form-control'}))
        self.fields['data_api_key-%s' % self.request.get_webid()] = forms.CharField(label="Data Store API Key:", widget=forms.TextInput(attrs={'class' : 'form-control'}))
        self.fields['date-%s' % self.request.get_webid()] = forms.DateField(label="Date:", widget = DateDropDownInput())

    def commit(self):
        # does the work of the form
        pass

    def as_full(self):
        # prints the form
        html = []

        # show hidden fields
        for field in self.hidden_fields():
            html.append('<p>')
            html.append('%s</p>' % field.label)
  
        # show non field errors       
        if self.errors:
            print(dir(self.non_field_errors))
            for error in self.errors:
                html.append('<p class="alert alert-danger" role="alert">')
                html.append('%s</p>' % error)
        
        # start of form header
        html.append('<form id="%s">' % self.request.get_webid())

        # displays field erros or help text if there are field errors
        for field in self.visible_fields():
            print(dir(field))
            html.append('<div class="form-group">')
            html.append('<label for="%s">%s</label>' % (field.id_for_label, field.label))
            html.append(field.as_widget())
            html.append('</div>')

            # show field errors
            if field.errors:
                for error in field.errors:
                    html.append('<div class="alert alert-danger" role="alert">')
                    html.append('%s</div>' % error) 

            # show help text
            if field.help_text:
                for help_text in field.help_text:
                    html.append('<p class="help-text">')
                    html.append('%s</p>' % help_text)

        # show submit button
        html.append('<input type="submit" class="btn btn-primary">')
            
        # form footer
        html.append('</form>')
        return '\n'.join(html)

    def add_fields_as_table(self, html, show_labels = True):
        """ Adds the html for all fields of a form """
        # hidden fields
        for field in self.hiddden_fields():
            self.add_field_as_table(html, field, False) # need to add this function
        # visible fields
        for field in self.visible_fields():
            self.add_field_as_table(html, field, show_labels)

    def add_field_as_table(self, html, field, show_labels = True):
        #do stuff here
        pass

    def __str__(self):
        return self.as_full()