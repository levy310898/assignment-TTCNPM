from django.shortcuts import render
# Create your views here.

def signUp(request):
    return render(request, 'home/sign-up.html')

def signIn(request):
    return render(request, "home/sign-in.html")

def home(request):
    return render(request,'home/home.html')

def myTest(request):
    return render(request,"home/my-test.html")