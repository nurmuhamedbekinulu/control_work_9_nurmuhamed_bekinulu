from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')
