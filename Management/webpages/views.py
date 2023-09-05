from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import ContactForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")

def feedback(request):
    return render(request,"pages/feedback.html")

def services(request):
    return render(request,"pages/services.html")

def update(request):
    return render(request,"pages/update.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request,"pages/contact.html",{'form':form})

def success(request):
   return HttpResponse('Success!')