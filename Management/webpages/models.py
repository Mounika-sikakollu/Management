from django.db import models
# Create your models here.

class Appointment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    number=models.IntegerField(help_text="Enter 10 digits numbers")
    message=models.TextField()

    def __str__(self):
        return self.name