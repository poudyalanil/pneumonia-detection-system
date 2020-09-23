from django.contrib.auth.backends import RemoteUserBackend
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate
from django.contrib import messages
# Create your views here.

def index(requests):
    return render(requests,'ums/index.html')

def sign_in(requests):
    if requests.POST:
        username = requests.POST['username']
        password = requests.POST['password']
        auth_user = authenticate(username=username,password=password)
        if auth_user:
            messages.success(requests,"Login Success")
            request.session['username'] = username
            # TODO
        else:
            messages.error(requests,"Incorrect Credentials")

    return render(requests,'ums/login.html')

def user_homepage(requests):
    return render(requests,'ums/dashboard.html')