from http.client import HTTPResponse
from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('add/', views.add_view, name='add'),
    path('delete/', views.delete_view, name='delete'),
]