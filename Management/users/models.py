from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.IntegerField(help_text="Enter 10 digits numbers")
    message=models.TextField()
   
    def __str__(self):
        return self.name

    

class Feedback(models.Model):
   full_name =models.CharField(max_length=100)
   email=models.EmailField()
   drname = models.CharField(max_length=100)
   services = models.TextField()
   date = models.DateTimeField(default=timezone.now)
   message = models.TextField()
     
   def __str__(self):
     return self.full_name







      
