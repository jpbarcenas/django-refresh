from datetime import date
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Employee

# Create your views here.
def employee_list(request):
    employees = Employee.objects.all()
    
    context = {
        'employees': employees,
    }

    return render(request, 'employee_list.html', context)


def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_details.html', {'employee': employee})


def employee_add(request):
    if request.method == 'POST':
        new_employee = Employee()
        new_employee.emp_id = request.POST['emp_id']
        new_employee.first_name = request.POST['first_name']
        new_employee.last_name = request.POST['last_name']
        new_employee.position = request.POST['position']
        new_employee.email = request.POST['email']
        new_employee.phone = request.POST['phone']
        
        if 'photo' in request.FILES:
            new_employee.photo = request.FILES['photo']
        
        new_employee.created_at = date.today()
        new_employee.updated_at = new_employee.created_at

        new_employee.save()
        return render(request, 'employee_details.html', {'employee': new_employee})
    else:
        return render(request, 'employee_add.html')


def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        new_employee = Employee()
        new_employee.id = employee.id
        new_employee.emp_id = request.POST['emp_id']
        new_employee.first_name = request.POST['first_name']
        new_employee.last_name = request.POST['last_name']
        new_employee.position = request.POST['position']
        new_employee.email = request.POST['email']
        new_employee.phone = request.POST['phone']
        
        if 'photo' in request.FILES:
            new_employee.photo = request.FILES['photo']
        else:
            new_employee.photo = employee.photo
        
        new_employee.created_at = employee.created_at
        new_employee.updated_at = date.today()

        new_employee.save()
        return render(request, 'employee_details.html', {'employee': new_employee})
    else:
        return render(request, 'employee_edit.html', {'employee': employee})