from django import forms
from django.forms import widgets

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'detailed_description', 'status', 'complete_date']
        error_messages = {
            'description': {
                'required': 'Заполните поле'
            },
            'status': {
                'required': 'Заполните поле'
            },
            'complete_date': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'description': widgets.Input(attrs={'class': 'form-control'}),
            'detailed_description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
            'complete_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }