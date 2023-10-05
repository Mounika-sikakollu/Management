from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

#class Contact(models.Model):
#    name=models.CharField(max_length=100)
#    email=models.EmailField()
#    phone_number=models.CharField(max_length=100)
#    message=models.TextField()
#    author=models.ForeignKey(User,on_delete=models.CASCADE)
#    def __str__(self):
#        return self.name

    

class Feedback(models.Model):
   fname =models.CharField(max_length=100)
   email=models.EmailField()
   drname = models.CharField(max_length=100)
   services = models.TextField()
   datef = models.DateTimeField(default=timezone.now)
   message = models.TextField()
   author=models.ForeignKey(User,on_delete=models.CASCADE)
   def __str__(self):
     return self.name







      
