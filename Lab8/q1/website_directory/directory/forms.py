from django import forms
from .models import Category, Page, General

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'visits', 'likes']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['category', 'title', 'url', 'views']

class GeneralForm(forms.ModelForm):
    class Meta:
        model = General
        fields = ['name', 'title', 'category', 'views']