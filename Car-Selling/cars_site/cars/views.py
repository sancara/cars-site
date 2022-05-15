from multiprocessing import context
from django.shortcuts import render
from . import models

# Create your views here.
def list_view(request):
    all_cars = models.Car.objects.all()
    context = {'todos_los_autos': all_cars}

    return render(request, 'cars/list.html', context=context)


def add_view(request):
    return render(request, 'cars/add.html')


def delete_view(request):
    return render(request, 'cars/delete.html')