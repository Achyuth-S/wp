from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name='employee_home'),  # Add this line
    path('insert/', views.insert_work_data, name='insert_work_data'),
    path('retrieve/', views.retrieve_employee_data, name='retrieve_employee_data'),
]