from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import News

#from .models import Category

# class NewsForm(forms.Form):
#    title = forms.CharField(max_length=150,
#                            label='Название',
#                            widget=forms.TextInput(attrs={"class": "form-control"}))
#    content = forms.CharField(label='Текст', required=False,
#                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
#    is_published = forms.BooleanField(label='Опубликовать', initial=True)
#    category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                      label='Категория',
#                                      empty_label='Выберите категорию',
#                                      widget=forms.Select(attrs={"class": "form-control"}))


# Форма Связано с model
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }