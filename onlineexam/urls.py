from django.contrib import admin
from django.urls import path,include
from onlineexam import views

urlpatterns = [
    path('', views.home, name="home"),
    path('registering/',views.registering,name="registering"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout")
]