from App1.models import Employee

# exec(open(r"D:\Shubham's Python Data\Shubham's_python\Django\first_project\App1\db_shell.py").read())

# all 
# all_emp = Employee.objects.all()
# print(all_emp)

# for emp in all_emp:
#     # print(emp)
#     print(emp.__dict__)

# single read
# try:
#     emp_obj = Employee.objects.get(id=5)
#     print(emp_obj)
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist")

# create emp
# 1st way
# emp_obj = Employee(first_name="D", last_name="E", email="d@gmail.com", salary=89000)
# emp_obj = Employee(first_name="oreo", last_name="o", email="o@gmail.com", salary=89000)
# emp_obj.save()

# 2nd way
# Employee.objects.create(first_name="python", last_name="language", email="py@gmail.com", salary=100000)

# update
# try:
#     emp_obj = Employee.objects.get(id=5)
#     emp_obj.salary = 55000
#     emp_obj.save()
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist")

# try:
#     emp_obj = Employee.objects.get(id=6)
#     emp_obj.last_name = "lang"
#     emp_obj.save()
# except Employee.DoesNotExist:
#     print("Employee with given id does not exist")

# delete
# try:
#     emp_obj = Employee.objects.get(id=7)
#     emp_obj.delete()
# except Employee.DoesNotExist:
#     print("Employee you want to delete does not exist")

# filter 
# gives empty set if no result found
# emp_obj = Employee.objects.filter(first_name__startswith="A")
# emp_obj = Employee.objects.filter(last_name__endswith="e")
# emp_obj = Employee.objects.filter(salary__lte=60000)
emp_obj = Employee.objects.filter(salary__gte=60000)
print(emp_obj)