from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'



class UserForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects, widget=forms.CheckboxSelectMultiple(), required=False)

    class Meta:
        model = User
        exclude=['user_id']
        widgets = {
            'birthday': DateInput(),
            'join_date': DateInput(),
        }



class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        exclude=['department_id']



