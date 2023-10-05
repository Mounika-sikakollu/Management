from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")


def services(request):
    return render(request,"pages/services.html")

def update(request):
    return render(request,"pages/update.html")

