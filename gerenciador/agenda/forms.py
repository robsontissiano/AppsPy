from django import forms
from django.forms import ModelForm
from agenda.models import ItemAgenda

class FormItemAgenda(forms.ModelForm):
	data = forms.DateField(
					widget=forms.DateInput(format="%d/%m/%Y"),
					input_formats=['%d/%m/%Y', '%d/%m/%y'])

	class Meta:
		model = ItemAgenda
		fields = ('titulo', 'data', 'descricao')

# class FormItemAgenda(forms.Form):
# 	titulo = forms.CharField(max_length=100)
# 	data = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),input_formats=['%d/%m/%y', '%d/%m/%Y'])
# 	hora = forms.TimeField()
# 	descricao = forms.CharField()