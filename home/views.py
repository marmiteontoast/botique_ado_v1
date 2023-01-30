from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def index(request):
    """ A view to return the index page """
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('the form is valid')
            messages.success(request, f'thank you well get back to you')
        
    else:
        form = ContactForm()

    return render(request, 'home/index.html', {
        'form': form
    })


