from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude=['user_id']
        widgets = {
            'birthday': DateInput(),
            'join_date': DateInput(),
        }

class RolesForm(forms.ModelForm): #Jo e perfunduar !!

    class Meta:
        model=UserRole
        exclude=['user_id','user_role_id']


class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        exclude=['department_id']

