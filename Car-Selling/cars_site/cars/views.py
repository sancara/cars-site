from django.shortcuts import render

# Create your views here.
def list_view(request):
    return render(request, 'cars/list.html')

def add_view(request):
    return render(request, 'cars/add.html')

def delete_view(request):
    return render(request, 'cars/delete.html')