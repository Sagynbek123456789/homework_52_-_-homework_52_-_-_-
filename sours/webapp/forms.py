from django import forms
from webapp.models import status_choices


class TaskForm(forms.Form):
    description = forms.CharField(max_length=60, required=True, label='Описание')
    status = forms.ChoiceField(choices=status_choices, label='Статус')
    date_of_completion = forms.DateField(required=False, label='Дата выполнения')
