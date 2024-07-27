from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            v.field.widget.attrs["class"] = "form-control"
            if isinstance(v.field, forms.EmailField):
                print(1)
                v.field.widget.attrs["required"] = True

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

        error_messages = {
            'email': {
                'required': 'Заполните поле'
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name and not last_name:
            raise ValidationError('Заполните поля имени или фамилии')
        return cleaned_data
