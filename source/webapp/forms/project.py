from django import forms
from django.forms import widgets

from webapp.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['name', 'description', 'started_at', 'ended_at']
        error_messages = {
            'name': {
                'required': 'Заполните поле'
            },
            'description': {
                'required': 'Заполните поле'
            },
            'started_at': {
                'required': 'Заполните поле'
            }
        }

        widgets = {
            'name': widgets.Input(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
            'started_at': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ended_at': widgets.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
