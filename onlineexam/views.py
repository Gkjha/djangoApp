from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .form import CreateUserForm
from django import forms
from .models import *



# Create your views here.

def home(request):
    return render(request,'index.html')

def registerPage(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1==password2:
            if user.object.filter(username=username).exists():
                print('username taken')
            elif user.object.filter(email=email).exists():
                print('email taken')
                user=user.object.create_user(username=username,email=email,password1=password1,password2=password2)
                user.save();
                print('user created')
        else:
            print('password notmatching')
        return redirect('home')

	
    return render(request, 'login1.html')

def loginPage(request):
		if request.method == 'POST':
			username = request.POST.get('username')
			password1 =request.POST.get('password1')

			student = authenticate(request, username=username, password1=password1)

			if student is not None:
				login(request, student)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def exam(request):
    return render(request,'exam.html')


def registering1(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
             
    context = {}
    return render(request, 'login1.html', context)

def registering(request):
    if request.method =='POST':
        username=request.POST('username')
        email=request.POST('email')
        password1=request.POST('password1')
        password2=request.POST('password2')

        if password1==password2:
            if student.object.filter(username=username).exists():
                print('username taken')
            elif student.object.filter(email=email).exists():
                print('email taken')
                student=student.object.create_user(username=username,email=email,password1=password1,password2=password2)
                student.save();
                print('user created')
        else:
            print('password notmatching')
        return redirect('home')
    context={}
    return render(request, 'login1.html',context)



	
		

		