from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_request, name = "sign-in"),
    path('home/user=<str:username>/', views.home, name= "home"),
    path('sign-up/', views.signUp, name= "sign-up"),
    path('home/user=<str:username>/my-test/', views.myTest, name= "my-test"),
    path('home/user=<str:username>/exam=<str:exam_name>/', views.doTest, name= "do-test"),
    path('admin/',views.admin,name="admin"),

]

