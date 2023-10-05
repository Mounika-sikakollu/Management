from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm
from django.http import HttpResponse
from.models import Feedback
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your account is created! you can login now')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def feedback(request):
    if request.method=="POST":
        fname=    request.POST["fname"]    
        email=    request.POST["email"]           
        services= request.POST["services"]    
        datef =   request.POST["datef"]     
        message = request.POST["message"]    
        obj=Feedback(fname=fname,email=email,services=services,datef=datef,message=message)
        obj.save()
        return HttpResponse("<h1> Feedback has been submitted </h1>")
    
    return render(request,'users/feedback.html')  
   
        
def profile(request):
    return render(request,'users/profile.html')

def contact(request):
   # if request.method=='POST':
   #     contact=Contact()
   #     name=request.POST('name')
   #     email=request.POST('email')
   #     phone_number=request.POST('phone_number')
   #     message=request.POST('message')
   #     contact.name=name
   #     contact.email=email
   #     contact.phone_number=phone_number
   #     contact.message=message
   #     contact.save()
    #    return HttpResponse("<h1> THANKS FOR CONTACT US </h1>")
    return render(request,"users/contact.html")

