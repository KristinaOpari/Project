from django.shortcuts import render

# relative import of forms
from .models import *
from .forms import *


def create_User(request):
    data = {}
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        data['form']=form

    return render(request, "create/createUser.html", data)


def create_Department(request):
    data = {}
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
    data['form'] = form
    return render(request, "create/createDepartment.html", data)