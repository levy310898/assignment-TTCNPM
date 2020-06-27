from django import forms

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangePassword
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User


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
                request.session['user'] = username
                return HttpResponseRedirect('/home/user=%s/' % username)
            else:
                # print('error')
                form = AuthenticationForm()
                context = {"error": "you might not register or password was wrong", "form":form}
                return render(request, 'home/sign-in.html', {"context":context})
                # messages.info(request, "cannot found your username or password")
        else:
            print('error')
            form = AuthenticationForm()
            context = {"error": "Invalid username or password.", "form":form}
            return render(request, 'home/sign-in.html', {"context":context})
            messages.info(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {"form":form}
    return render(request, 'home/sign-in.html', {"context":context})
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
            #new add by An 23/06/2020
            username = request.POST['username']
            user = User.objects.get(username = username)
            info = Info()
            info.key = user
            info.save()
            #new add by An 23/06/2020
            return HttpResponseRedirect('/home/user=%s/' % request.POST['username'])
    return render(request, 'home/sign-up.html', {'form': form})

def home(request,username):
    # return render(request,"home/home.html")
    user = User.objects.get(username = username)
    exams = Exam.objects.exclude(key = user)
    exams_context = []
    for exam in exams:
        creator = exam.key
        score_obj = []
        # score_obj = Point.objects.get(key1 = creator, key2 = exam)
        for score in Point.objects.filter(key1 = user,key2 = exam):
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

def myTest(request, username):
    user = request.session.get('user', None)
    print('user')
    if user is None or user == '' or user == []:
        return redirect(reverse('sign-in'))
    user = User.objects.get(username = username)
    my_exams = Exam.objects.filter(key=user)
    my_exams_context = []
    print('123')
    for exam in my_exams:
        my_exams_context.append({
            "exam":exam.examName
        })
    
    do_exams = Exam.objects.exclude(key = user)# lấy ra những exams không phải do user này tạo ra
    done_exams_context = []
    for exam in do_exams:
        creator = exam.key
        score_obj = []
        # score_obj = Point.objects.get(key1 = creator, key2 = exam)
        for score in Point.objects.filter(key1 = user,key2 = exam):
            score_obj.append(score)
        score = None
        if score_obj ==[]:
            pass
        else:
            scores = []# lấy điểm số lớn nhất
            for item in score_obj:
                scores.append(item.point)
            score = max(scores)
            done_exams_context.append({
                "creator":creator.username,
                "exam":exam.examName,
                "score":score,
            })
    context = {
        "username": username,
        "my_exams":my_exams_context,
        "done_exams":done_exams_context,
    }
    return render(request,"home/my-test.html",{"context":context})

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
        point.point = "%.2f" % (no_corr_chooseAns/len(corrAns)*10)
        point.save()
        return HttpResponseRedirect('/home/user=%s/' % username)
    return render(request,'home/do-test.html',context)

def info(request, username):
    user = User.objects.get(username = username)
    info = Info.objects.get(key = user.id)
    context = {
        'firstName' : user.first_name,
        'lastName' : user.last_name,
        'sex' : info.sex,
        'address' : info.address,
        'birthDate' : info.birthDate,
    }
    print(info.birthDate)

    if request.method == 'POST':
        user.first_name = request.POST['firstName']
        user.last_name = request.POST['lastName']
        user.save()
        info.sex = request.POST['sex']
        info.address = request.POST['address']
        if request.POST['birthDate'] != "":
            info.birthDate = request.POST['birthDate']
            print('birth date: ' + request.POST['birthDate'])
        else:
            info.birthDate = info.birthDate
            # print('birth date fail: ' + info.birthDate.strftime(' %d / %m / %Y'))
        # print('first ' + info.birthDate.strftime(' %d / %m / %Y'))
        info.save()
        # print('first ' + info.birthDate.strftime(' %d / %m / %Y'))
        
        context = {
            'firstName' : user.first_name,
            'lastName' : user.last_name,
            'sex' : info.sex,
            'address' : info.address,
            'birthDate' : info.birthDate,
        }
        return render(request, 'home/info.html',context)

    return render(request, 'home/info.html', context)
def change_password(request,username):
        form=ChangePassword(request.POST, username)
        user = User.objects.get(username = username)
        if request.method=='POST':
            if form.is_valid():
                new_pass=form.cleaned_data['new_password']
                  #get the current user object as user
                
                user.password=new_pass 
                print('pasword la ' + new_pass + 'user la: ' + user.username)
                user.save()
                print('password moi la ' + user.password)
                return HttpResponseRedirect('/home/user=%s/' % username)
        return render(request, 'home/change-password.html', {'form': form})          #do whatever you want to do man..


def add_my_test(request, username):
    data = request.POST
    try:
        user = User.objects.get(username = username)
    except:
        return redirect(reverse('sign-in'))
    my_exam = Exam.objects.create(
        key=user,
        examName=data.get('testname', None)
    )
    # return redirect('/home/user='+ username +'/my-test/')
    #return render(request,'/home/user=%s/make-test.html' %username)
    return render(request,'home/make-test.html',{"my_exam":my_exam})

def add_my_question(request,username,examname):
    try:
        exam = Exam.objects.get(examName=examname)
    except Exception as e:
        print(e)
        return redirect(reverse('sign-in'))
    if request.method == 'GET':
        question = Question.objects.filter(key=exam).first()
        return render(request,'home/make-test.html',{"my_exam":exam, "question": question})
    else:
        data = request.POST
        question = Question.objects.filter(key=exam).first()
        if question:
            print(question)
            question.question = data.get('ques', question.question)
            question.answerA = data.get('answerA', question.answerA)
            question.answerB = data.get('answerB', question.answerB)
            question.answerC = data.get('answerC', question.answerC)
            question.answerD = data.get('answerD', question.answerD)
            question.corrAns = data.get('correct', question.corrAns)
            question.save()
        else:
            my_question=Question.objects.create(
                key=exam,
                question=data.get('ques',None),
                answerA=data.get('answerA',None),
                answerB=data.get('answerB',None),
                answerC=data.get('answerC',None),
                answerD=data.get('answerD',None),
                corrAns=data.get('correct',None),
            )
            #return HttpResponse("thêm câu hỏi thành công")
        return redirect('/home/user='+ username + '/my-test')