from django import forms
from django.forms import widgets

from webapp.models import Task


def description_length_validate(description):
    if len(description) < 3:
        raise forms.ValidationError("Минимум 3 символа!")


def description_value_validate(description):
    if description == 'Bektur':
        raise forms.ValidationError("Введите другое описание!")


class TaskForm(forms.ModelForm):
    description = forms.CharField(max_length=200, required=True, label='Описание',
                                  validators=[description_length_validate, description_value_validate])

    class Meta:
        model = Task
        fields = ['description', 'detailed_description', 'status', 'types']
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
        }

        widgets = {
            'description': widgets.Input(attrs={'class': 'form-control'}),
            'detailed_description': widgets.Textarea(attrs={'class': 'form-control', 'cols': 50, 'rows': 5}),
            'status': widgets.Select(attrs={'class': 'form-control'}),
            'types': widgets.CheckboxSelectMultiple(),
        }