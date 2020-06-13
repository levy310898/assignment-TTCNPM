from django import forms
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return HttpResponseRedirect('/home/home')
                
    
            else:
                messages.info(request, "Invalid username or password.")
        else:
            messages.info(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'home/sign-in.html', {"form":form})
def home(request):
    return render(request,'home/home.html')

def signUp(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/home')
    return render(request, 'home/sign-up.html', {'form': form})