from django.contrib.auth.backends import RemoteUserBackend
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate, logout
from django.contrib import messages
# Create your views here.


######################
##### general   ####
######################
def index(requests):
    #url: /
    return render(requests,'ums/index.html')

def sign_in(requests):
      #url: /login
    if requests.POST:
        username = requests.POST['username']
        password = requests.POST['password']
        auth_user = authenticate(username=username,password=password)
        if auth_user:
            messages.success(requests,"Login Success")
            requests.session['username'] = username

            return redirect('user_homepage')
            # TODO
        else:
            messages.error(requests,"Incorrect Credentials")

    return render(requests,'ums/login.html')

def logout(requests):
    #url: /logout
    logout(requests)
    return redirect('homepage')



######################
##### user side   ####
######################

def user_homepage(requests):
      #url: /usr/home
      #TODO
    return render(requests,'ums/dashboard.html')

def all_patients(requests):
      #url: /usr/patients/
      #TODO
      pass

def new_test(requests):
      #url: /usr/new/
      #TODO
      pass

def stats(requests):
      #url: /usr/stats/
      #TODO
      pass

def support(requests):
      #url: /usr/support/
      #TODO
      pass

def user_profile(requests):
      #url: /usr/profile/<id>
      #TODO
      pass
def edit_profile(requests):
    #url: /usr/profile/edt/<id>
    #TODO
    pass





######################
##### admin side  ####
######################

def new_user(requests):
      #url: /admin/new-usr/
      #TODO
    return render(requests,"ums/new_user.html")

def delete_user(requests):
      #url: /admin/usr/del/<id>
        #TODO
      pass
def edit_user(request):
      #url: /admin/usr/edit/<id>
      #TODO
      pass



