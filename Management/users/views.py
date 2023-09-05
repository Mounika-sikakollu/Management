from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import UserRegisterForm,ContactForm
from django.http import HttpResponse


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