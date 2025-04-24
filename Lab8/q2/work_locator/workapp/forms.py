from django import forms
from .models import WORKS

class WorkForm(forms.ModelForm):
    class Meta:
        model = WORKS
        fields = ['person_name', 'company_name', 'salary']

class CompanyQueryForm(forms.Form):
    company_name = forms.CharField(label='Company Name', max_length=100)