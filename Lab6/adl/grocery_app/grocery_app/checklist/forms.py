from django import forms
from .models import GroceryItem

class GroceryItemForm(forms.Form):
    items = forms.ModelMultipleChoiceField(
        queryset=GroceryItem.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )