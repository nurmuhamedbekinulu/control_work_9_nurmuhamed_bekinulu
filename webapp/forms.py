from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, BaseValidator
from webapp.models.photos import Photo


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Найти')


def max_len_validator(string):
    if len(string) > 20:
        raise ValidationError('Описание должено быть длиннее 2 символов')
    return string


class CustomLenValidator(BaseValidator):
    def __init__(self, limit_value=200):
        message = 'Максимальная длина описания %(limit_value)s. Вы ввели %(show_value)s символов'
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        print(value)
        print(limit_value)
        return value > limit_value

    def clean(self, value):
        return len(value)


class PhotoForm(forms.ModelForm):
    caption = forms.CharField(
        validators=(MinLengthValidator(limit_value=2, message='как минимум 2 символа'), CustomLenValidator()))

    class Meta:
        model = Photo
        fields = ('photo', 'caption', 'author')
        widgets = { 'photo': forms.ClearableFileInput(attrs={'multiple': True}),}
        labels = {
            'photo': 'Фотография',
            'caption': 'Описание',
            'author': 'Автор',
        }

    def clean_caption(self):
        caption = self.cleaned_data.get('caption')
        if len(caption) < 2:
            raise ValidationError('Описание должено быть длиннее 2 символов')
        if Photo.objects.filter(caption=caption).exists():
            raise ValidationError('Картинка с таким описанием уже есть')
        return caption
