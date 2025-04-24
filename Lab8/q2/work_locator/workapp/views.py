from django.shortcuts import render, redirect
from .forms import WorkForm, CompanyQueryForm
from .models import WORKS, LIVES

def index(request):
    work_form = WorkForm()
    query_form = CompanyQueryForm()

    if request.method == 'POST':
        if 'add_work' in request.POST:
            work_form = WorkForm(request.POST)
            if work_form.is_valid():
                work_form.save()
                return redirect('index')

        elif 'query_company' in request.POST:
            query_form = CompanyQueryForm(request.POST)
            if query_form.is_valid():
                company = query_form.cleaned_data['company_name']
                employees = WORKS.objects.filter(company_name=company)
                data = []
                for emp in employees:
                    lives = LIVES.objects.filter(person_name=emp.person_name).first()
                    city = lives.city if lives else 'Unknown'
                    data.append((emp.person_name, city))
                return render(request, 'workapp/results.html', {
                    'company': company,
                    'data': data
                })

    return render(request, 'workapp/index.html', {
        'work_form': work_form,
        'query_form': query_form
    })