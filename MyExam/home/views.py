from django import forms
from django.shortcuts import render

from .forms import RegistrationForm
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
# Create your views here.

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
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

def home(request):
    return render(request,'home/home.html')

def myTest(request):
    return render(request,"home/my-test.html")
def doTest(request, exam_name):
    exam = Exam.objects.get(examName = exam_name) #get the exam
    ques = list(Question.objects.filter(key = exam.id)) #find all of the question related to that exam
    context = {
        'question' : ques,
    }
    return render(request,'home/do-test.html',context)
