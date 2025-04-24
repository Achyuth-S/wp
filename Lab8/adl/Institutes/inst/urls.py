from django.urls import path
from . import views

urlpatterns = [
    path('institutes/', views.show_institutes, name='show_institutes'),
]
