

from django.shortcuts import render

from employees.models import Employee


def home(request):
    return render(request, 'home.html')
