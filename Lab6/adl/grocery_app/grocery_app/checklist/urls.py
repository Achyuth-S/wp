from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path('', views.grocery_checklist, name='grocery_checklist'),
     path('', lambda request: redirect('igrocery_checklist'), name='home'),

]