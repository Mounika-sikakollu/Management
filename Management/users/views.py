from django.shortcuts import HttpResponse,render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm
from .models import Feedback,Contact
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
        full_name=request.POST.get("full_name")    
        email=request.POST.get("email")        
        services=request.POST.get("services")    
        date=request.POST.get("date") 
        message=request.POST.get("message")   
        obj=Feedback(full_name=full_name,email=email,services=services,date=date,message=message)
        obj.save()
        return HttpResponse("<h1> Feedback has been submitted </h1>")
    
    return render(request,'users/feedback.html')  
   
        
def profile(request):
    return render(request,'users/profile.html')

def contact(request):
     if request.method=="POST":
         contact=Contact()
         name=request.POST.get('name')
         email=request.POST.get('email')
         phone_number=request.POST.get('phone_number')
         message=request.POST.get('message')
         contact.name=name
         contact.email=email
         contact.phone_number=phone_number
         contact.message=message
         contact.save()
         return HttpResponse("<h1> THANKS FOR CONTACT US </h1>")
     
     return render(request,"users/contact.html")
  