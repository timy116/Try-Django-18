from django.shortcuts import render
from newsletter.forms import SignUpForm, ContactForm


def index(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'index.html', {'form': form, 'title': 'Welcome'})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for k, v in form.cleaned_data.items():
            print(k, v)
    return render(request, 'forms.html', {'form': form, 'title': 'Contact Us ...'})
