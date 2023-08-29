from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employee, City
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/")
def search_emp(request):
    employees = Employee.objects.all()
    context = {'Employees': employees}
    return render(request, 'employee/search.html', context)

@login_required(login_url="/")
def create_emp(request):
    form = EmployeeForm()
    if request.method == "POST":
        if Employee.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, "Employee alredy Exist")
            return redirect('create')
        else:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Employee created")
                return redirect('search')
    context = {'form': form}
    return render(request, 'employee/create.html', context)

@login_required(login_url="/")
def update_emp(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Details Updated")
            return redirect('search')
        
    context = {'form': form}
    return render(request, 'employee/create.html', context)

@login_required(login_url="/")
def delete_emp(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    messages.success(request, "Employee Deleted")
    return redirect('search')

# AJAX
@login_required(login_url="/")
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return JsonResponse(list(cities.values('id', 'name')), safe=False)
