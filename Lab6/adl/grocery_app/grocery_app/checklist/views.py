from django.shortcuts import render
from .forms import GroceryItemForm

def grocery_checklist(request):
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            selected_items = form.cleaned_data['items']
            return render(request, 'checklist/checklist.html', {'selected_items': selected_items})
    else:
        form = GroceryItemForm()
    return render(request, 'checklist/item_selection.html', {'form': form})