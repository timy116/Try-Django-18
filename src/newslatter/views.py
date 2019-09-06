from django.shortcuts import render
from newslatter.forms import SignUpForm


def index(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'index.html', {'form': form})
