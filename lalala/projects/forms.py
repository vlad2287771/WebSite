from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text',
                 'date'
                       ]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка'
            }),
           "date": DateTimeInput(attrs={
               'class': 'form-control',
               'placeholder': 'Дата публикации'
           }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание проекта'
            }),
        }