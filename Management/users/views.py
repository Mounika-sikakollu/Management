from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm,ContactForm
from django.http import HttpResponse
from.models import Post
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
   context={
      'posts': Post.objects.all()
   }
   return render(request,"users/feedback.html",context)

def profile(request):
    return render(request,'users/profile.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request,"users/contact.html",{'form':form})

def success(request):
   return HttpResponse('Success!')