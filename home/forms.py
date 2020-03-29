from .models import Country
from django.forms import ModelForm, TextInput

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
            'class': 'form-control mr-sm-2',
            'name': 'country',
            'placeholder': 'Write country...'
        })}