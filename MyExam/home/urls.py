from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.login_request, name = "sign-in"),
    path('home/user=<str:username>/', views.home, name= "home"),
    path('sign-up/', views.signUp, name= "sign-up"),
    path('home/user=<str:username>/my-test/', views.myTest, name= "my-test"),
    path('home/user=<str:username>/my-test/add', views.add_my_test, name= "add-my-test"),
    path('home/user=<str:username>/exam=<str:exam_name>/', views.doTest, name= "do-test"),
    path('admin/',views.admin,name="admin"),
    path('',views.logout, {'next/page':'/'}, name='logout'),
    path('home/user=<str:username>/info/', views.info, name='info'),
    path('home/user=<str:username>/change-password/', views.change_password, name='change-password'),
<<<<<<< HEAD
    path('home/user=<str:username>/examname=<str:examname>/add-question/',views.add_my_question,name="add-question"),
=======
    path('home/user=<str:username>/info/',views.info, name = "info"),
>>>>>>> d38018d5e89977a087d03f8e17dd66cc286b77f1
]

