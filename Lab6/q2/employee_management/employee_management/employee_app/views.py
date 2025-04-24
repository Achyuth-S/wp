from django.shortcuts import render, redirect
from .forms import WorksForm, CompanyForm
from .models import Works, Lives
from django.db.models import Q

def insert_work_data(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'insert_success.html')
    else:
        form = WorksForm()
    return render(request, 'insert_work.html', {'form': form})

def retrieve_employee_data(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company_name']
            employees = Works.objects.filter(company_name__iexact=company)
            employee_data = []
            for employee in employees:
                employee_data.append({
                    'name': employee.person_name,
                    'city': employee.city
                })
            return render(request, 'retrieve_results.html', {'employees': employee_data, 'company': company})
    else:
        form = CompanyForm()
    return render(request, 'retrieve_form.html', {'form': form})

def employee_home(request):
    return render(request, 'employee_home.html')