from django import forms
from django.forms import widgets

from webapp.models import Task, Type


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'detailed_description', 'status', 'types', 'complete_date']
        error_messages = {
            'description': {
                'required': 'Заполните поле'
            },
            'status': {
                'required': 'Заполните поле'
            },
            'types': {
                'required': 'Заполните поле'
            },
            'complete_date': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'description': widgets.Input(attrs={'class': 'form-control'}),
            'detailed_description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
            'status': widgets.Select(attrs={'class': 'form-control'}),
            'types': widgets.CheckboxSelectMultiple(attrs={'class': ''}),
            'complete_date': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }