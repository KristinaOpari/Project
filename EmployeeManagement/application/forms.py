from django import forms
from django.forms import widgets

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
# creating a form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude=['user_id']
        widgets = {
            'birthday': DateInput(),
            'join_date': DateInput(),
        }

