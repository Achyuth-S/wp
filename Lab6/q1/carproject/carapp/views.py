from django.shortcuts import render
from .models import Car

def car_form(request):
    manufacturers = ['Toyota', 'Honda', 'Ford', 'BMW', 'Tesla']
    return render(request, 'carapp/form.html', {'manufacturers': manufacturers})

def car_result(request):
    if request.method == 'GET':
        manufacturer = request.GET.get('manufacturer')
        model = request.GET.get('model')

        if manufacturer and model:
            Car.objects.create(manufacturer=manufacturer, model=model)

        return render(request, 'carapp/result.html', {
            'manufacturer': manufacturer,
            'model': model
        })
    