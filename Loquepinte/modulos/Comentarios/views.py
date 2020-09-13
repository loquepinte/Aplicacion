from django.shortcuts import render
from .models import Restaurant
def hola(request):
    variable= Restaurant.objects.all

