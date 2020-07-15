from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
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
    path('home/user=<str:username>/examname=<str:examname>/add-question/',views.add_my_question,name="add-question"),
    path('home/user=<str:username>/search/',views.search, name = "search"),
    path('home/user=<str:username>/newTest/',views.newTest,name = "new test"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

