from django.urls import path
from . import views
urlpatterns = [
    path('sign-in/', views.signIn, name = "sign-in"),
    path('home/', views.home, name= "home"),
    path('sign-up/', views.signUp, name= "sign-up"),
    path('my-test/',views.myTest,name = "my_test")

]

