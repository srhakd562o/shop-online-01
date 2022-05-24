from django.shortcuts import render, redirect
from django.views import View

def contact(request):
    return render(request, 'contact.html')