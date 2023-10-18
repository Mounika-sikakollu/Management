from django.shortcuts import  HttpResponse, render,redirect
from .models import Appointment


# Create your views here.

def home(request):
     if request.method=="POST":
         appiontment=Appointment()
         name=request.POST.get('name')
         email=request.POST.get('email')
         number=request.POST.get('number')
         message=request.POST.get('message')
         appiontment.name=name
         appiontment.email=email
         appiontment.number=number
         appiontment.message=message
         appiontment.save()
         return HttpResponse("<h1> THANKS FOR APPOINTMENT US </h1>")
     
     return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")


def services(request):
    return render(request,"pages/services.html")

def news(request):
    return render(request,"pages/news.html")

def more(request):
    return render(request,"pages/more.html")