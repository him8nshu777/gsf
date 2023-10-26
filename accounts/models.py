from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.username
    