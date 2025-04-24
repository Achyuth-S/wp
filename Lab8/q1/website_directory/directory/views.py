from django.shortcuts import render, redirect
from .models import Category, Page, General
from .forms import CategoryForm, PageForm, GeneralForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'directory/index.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'directory/add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request, 'directory/add_page.html', {'form': form})


def add_general(request):
    if request.method == 'POST':
        form = GeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GeneralForm()
    return render(request, 'directory/add_general.html', {'form': form})