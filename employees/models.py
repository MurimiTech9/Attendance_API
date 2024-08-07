from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

 # Employee class model   
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    department = models.CharField(max_length=100) #department of the employee
    name = models.CharField(max_length=100) #employee name
    email = models.EmailField(max_length=100) #email of the employee
    phone = models.CharField(max_length=100) #phone number of the employee


    def __str__(self):
        return self.user.username