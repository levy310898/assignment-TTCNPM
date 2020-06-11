from django.shortcuts import render
from .models import *
# Create your views here.

def signUp(request):
    return render(request, 'home/sign-up.html')

def signIn(request):
    return render(request, "home/sign-in.html")

def home(request):
    return render(request,'home/home.html')

def myTest(request):
    return render(request,'home/my-test.html')

def doTest(request, exam_name):
    exam = Exam.objects.get(examName = exam_name) #get the exam
    ques = list(Question.objects.filter(key = exam.id)) #find all of the question related to that exam
    context = {
        'question' : ques,
    }
    return render(request,'home/do-test.html',context)