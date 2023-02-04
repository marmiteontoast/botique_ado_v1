from django import forms
from django.forms import ModelForm


from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Contact
        fields = ('name', 'email')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'name'}),
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-2', 'placeholder': 'email'}),
        