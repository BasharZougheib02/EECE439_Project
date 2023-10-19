from django import forms
from .models import Contactlist
class CreateContactForm(forms.Form):
 model = Contactlist
 id = forms.IntegerField(label='ID', min_value=0)
 name = forms.CharField(label='Name')
 address = forms.CharField(label='Address')
 profession = forms.CharField(label='Profession')
 profession2 = forms.CharField(label='Profession 2')
 number = forms.CharField(label='Number')
 email = forms.CharField(label='Email')

class UpdateContactForm(forms.Form):
 name = forms.CharField(label='Name', required=False)
 address = forms.CharField(label='Address', required=False)
 profession = forms.CharField(label='Profession', required=False)
 profession2 = forms.CharField(label='Profession 2', required=False)
 number = forms.CharField(label='Number', required=False)
 email = forms.CharField(label='Email', required=False)