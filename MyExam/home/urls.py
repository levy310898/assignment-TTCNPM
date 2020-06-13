from django.urls import path
from . import views
urlpatterns = [
    path('signin/', views.login_request, name = "sign-in"),
    path('home/', views.home, name= "home"),
    path('signup/', views.signUp, name= "sign-up"),

]

