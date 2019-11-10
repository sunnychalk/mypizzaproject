from django import forms
from django.forms import ModelForm
from dishes.models import Drink

class ContactForm(forms.Form):
	name = forms.CharField(help_text='Help Text', required=False)
	message = forms.CharField(widget=forms.Textarea, max_length=256, min_length=10)

	def send_email(self):
		print('self.cleaned_data', self.cleaned_data)

class DrinkForm(forms.ModelForm):
	class Meta:
		model = Drink
		fields = ['name', 'price']