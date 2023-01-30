from django import forms

from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Contact
        fields = ('name', 'email')
        labels = {
            'name': '', 
            'email': ''
        }