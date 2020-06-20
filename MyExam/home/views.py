from django import forms
from django.shortcuts import render

from .forms import RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

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
                print(user.username)
                # return HttpResponseRedirect("/home")
                # return home(request,username)
                return HttpResponseRedirect('/home/user=%s/' % username)
            else:
                print('error')
                form = AuthenticationForm()
                context = {"error": "Invalid username or password.", "form":form}
                return render(request, 'home/sign-in.html', {"context":context})
                messages.info(request, "Invalid username or password.")
        else:
            print('error')
            form = AuthenticationForm()
            context = {"error": "Invalid username or password.", "form":form}
            return render(request, 'home/sign-in.html', {"context":context})
            messages.info(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'home/sign-in.html', {"form":form})
# def home(request):
#     return render(request,'home/home.html')

def admin(request):
    return HttpResponse('/admin')

def signUp(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/user=%s/' % request.POST['username'])
    return render(request, 'home/sign-up.html', {'form': form})

def home(LoginRequiredMixin,request,username):
    # return render(request,"home/home.html")
    user = User.objects.get(username = username)
    exams = Exam.objects.all()
    exams_context = []
    for exam in exams:
        creator = exam.key
        score_obj = []
        # score_obj = Point.objects.get(key1 = creator, key2 = exam)
        for score in Point.objects.filter(key1 = creator, key2 = exam):
            score_obj.append(score)
        print(score_obj)
        score = None
        if score_obj ==[]:
            score = "chua lam"
        else:
            scores = []
            for item in score_obj:
                scores.append(item.point)
            score = max(scores)
        exams_context.append({
            "user_name":creator.username,
            "exam":exam.examName,
            "score":score,
        })    
    
    context = {
        "user":user,
        "exams" : exams_context,
    }
    return render(request,'home/home.html',{"context":context})

def myTest(request):
    return render(request,"home/my-test.html")
def doTest(request, username, exam_name):
    exam = Exam.objects.get(examName = exam_name) #get the exam
    ques = list(Question.objects.filter(key = exam.id)) #find all of the question related to that exam
    context = {
        "exam_name":exam_name,
        'question' : ques,
    }
    if request.method == 'POST':
        corrAns = []
        chooseAns = []
        no_corr_chooseAns = 0
        for q in ques:
            corrAns.append(q.corrAns)
            if q.question in request.POST:
                chooseAns.append(request.POST[q.question])
            else:
                chooseAns.append("")
        for i in range(len(chooseAns)):
            if chooseAns[i] == corrAns[i]:
                no_corr_chooseAns += 1
        point = Point()
        user = User.objects.get(username = username)
        point.key1 = user
        point.key2 = exam
        point.point = no_corr_chooseAns
        point.save()
    return render(request,'home/do-test.html',context)
