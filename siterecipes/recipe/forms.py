from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Recipe, Category


class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категория')

    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'ingredients', 'time_to_cook', 'content', 'cat', 'tags', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredients': forms.TextInput(attrs={'class': 'form-control'}),
            'time_to_cook': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),

        }


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Файл')
