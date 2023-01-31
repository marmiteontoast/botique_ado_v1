from django import forms
from django.forms import ModelForm

from .models import Contact


class ContactForm(ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Contact
        fields = ('name', 'email')
        labels = {
            'name': '', 
            'email': ''
        }