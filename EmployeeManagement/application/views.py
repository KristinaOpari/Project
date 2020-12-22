from django.shortcuts import render

# relative import of forms
from .models import *
from .forms import *


def create_view(request):
    data = {}
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, "create.html", data)