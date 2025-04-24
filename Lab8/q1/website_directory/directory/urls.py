from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/', views.add_page, name='add_page'),
    path('add_general/', views.add_general, name='add_general'),
]