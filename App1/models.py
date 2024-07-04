from django.db import models

# Create your models here.


class Employee(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_num = models.BigIntegerField(unique=True, null=True)   #BigIntegerField -- for more length numbers
    designation = models.CharField(max_length=100, null=True)
    salary = models.IntegerField()
    date_joined = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.first_name
    
    def __repr__(self):
        return str(self)
    
    class Meta:
        db_table = "employee"