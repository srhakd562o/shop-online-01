from django.shortcuts import render, redirect
from django.views import View

def house(request):
    return render(request, 'house.html')