from django.shortcuts import render
from .models import Institute

def show_institutes(request):
    institutes = Institute.objects.all()
    return render(request, 'institutes/dropdown.html', {'institutes': institutes})
