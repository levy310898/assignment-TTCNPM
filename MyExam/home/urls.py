from django.urls import path
from . import views
urlpatterns = [
    path('sign-in/', views.login_request, name = "sign-in"),
    path('home/', views.home, name= "home"),
    path('sign-up/', views.signUp, name= "sign-up"),
    path('my-test/', views.myTest, name= "my-test"),
    path('home/<str:exam_name>/', views.doTest, name= "do-test"),

]

