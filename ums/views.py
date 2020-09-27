from django.contrib.auth.backends import RemoteUserBackend
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate, logout, login
from django.contrib import messages
from .forms import Register_Form, Normal_User_Form 
from django.contrib.auth.models import User
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
            # requests.session['username'] = username
            login(requests,auth_user)
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
    return render(requests,'ums/user/user_dashboard.html')

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

def admin_dashboard(requests):
      return render(requests,'ums/admin/admin_dashboard.html')

def new_user(requests):
      if requests.POST:
            main_form  = Register_Form(requests.POST)
            normal_form = Normal_User_Form(requests.POST)

            try:
                  user = User.objects.get(username= requests.POST['username'])
                  return HttpResponse("User already exists you moroon!!")
            except  User.DoesNotExist:
                  if main_form.is_valid() and normal_form.is_valid():
                        user = main_form.save()
                        normal_user = normal_form.save(commit=False)
                        normal_user.user= user
                        normal_user.save()


                        username = main_form.cleaned_data.get('username')
                        password = main_form.cleaned_data.get('password')

                        user = authenticate(username=username,password=password)
                        login(requests,user)
                        return redirect(new_user)
      else:
            main_form = Register_Form()
            normal_form = Normal_User_Form()
      context = {'main_form':main_form,'normal_form':normal_form}
                  
      return render(requests,"ums/admin/new_user.html",context)

def delete_user(requests, pk):
      user = User.objects.get(pk=pk)
      print(pk)
      user.delete()
      return redirect('all_users')
      #url: /admin/usr/del/<id>
     
def edit_user(request):
      #url: /admin/usr/edit/<id>
      #TODO
      pass

def all_users(requests):
      users = User.objects.all()
      return render(requests,"ums/admin/manage_users.html",{'users':users})


