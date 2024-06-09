from django.shortcuts import render
from cars.models import Car

def car_view(request):
    #print(request)
    print(request.GET)
    #print(request.GET).get('search')
    #cars = Car.objects.filter(factory_year=2015)
    cars = Car.objects.all() # Seleciona todos os registros da tebela
    #print(cars[1])



    return render(
        request,
        'cars.html',
        {'cars': cars })
        #{'cars': {'model': 'Kwid 2024'}})

