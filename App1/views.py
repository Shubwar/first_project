from django.shortcuts import render, redirect
# from django.http import request
from .models import Employee

# Create your views here.

def get_employees(request):
    all_emps = Employee.objects.all()
    return render(request=request, template_name="employees.html", context={"all_emps":all_emps})

def get_employee():
    pass

def create_employee(request):
    # print(request.POST)
    if request.method == "POST":
        if not request.POST.get("id"):
            Employee.objects.create(first_name=request.POST.get("fname"),
                                    last_name=request.POST.get("lname"),
                                    email=request.POST.get("em"),
                                    mobile_num=request.POST.get("mb"),
                                    designation=request.POST.get("dsn"),
                                    salary=request.POST.get("sal"))
            # return redirect("get_emps")
        else:
            emp = Employee.objects.get(id=request.POST.get("id"))
     
            emp.first_name = request.POST.get("fname")
            emp.last_name = request.POST.get("lname")
            emp.email = request.POST.get("em")
            emp.mobile_num = request.POST.get("mb")
            emp.designation = request.POST.get("dsn")
            emp.salary = request.POST.get("sal")
            emp.save()

        return redirect("get_emps")
        
    elif request.method == "GET":
        return render(request, "create_employee.html")

def employee(request, eid):
    emp = Employee.objects.get(id=eid)
    return render(request, "create_employee.html", {"single_emp": emp})

def update_employee(request, eid):
    pass

def delete_employee(request, eid):
    emp = Employee.objects.get(id=eid)

    emp.delete()
    return redirect("get_emps")
