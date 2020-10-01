from django.contrib.auth.backends import RemoteUserBackend
from django.db.models.aggregates import Count
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate, logout, login
from django.contrib import messages
from .forms import Register_Form, Normal_User_Form, User_Update_Form,Normal_User_Update_Form
from django.contrib.auth.models import User
from .models import Normal_User
from django.core.mail import send_mail
# from .decorators import login_required

from django.contrib.auth.decorators import login_required
from .decorators import admin_required
import random, string
import os
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

            if requests.user.is_staff:
                  return redirect("admin_dashboard")
            else:

                  return redirect('user_homepage')
            # TODO
        else:
            messages.error(requests,"Incorrect Credentials")

    return render(requests,'ums/login.html')

@login_required(login_url='/login')
def log_out(requests):
    #url: /logout
    logout(requests)
    return redirect('homepage')

def request_user_register(requests):


      pass




######################
##### user side   ####
######################
@login_required(login_url='/login')
def user_homepage(requests):
      #url: /usr/home
      #TODO
    return render(requests,'ums/user/user_dashboard.html')

@login_required(login_url='/login')
def all_patients(requests):
      #url: /usr/patients/
      #TODO
      pass
@login_required(login_url='/login')
def new_test(requests):
      #url: /usr/new/
      #TODO
      pass
@login_required(login_url='/login')
def stats(requests):
      #url: /usr/stats/
      #TODO
      pass
@login_required(login_url='/login')
def support(requests):
      #url: /usr/support/
      #TODO
      pass
@login_required(login_url='/login')
def user_profile(requests):
      user = requests.user
      return render(requests,"ums/user/user_profile.html",context={'user':user})
      

      pass
@login_required(login_url='/login')
def edit_profile(requests):
    #url: /usr/profile/edt/<id>
      user = requests.user
      # print(user)
      # print(pk)
      # register_form = User_Update_Form
      # normal_form =Normal_User_Update_Form

      print(user.normal_user.phone)
      
      if requests.POST:
                  
            update_user_form = User_Update_Form(data=requests.POST, instance=user)
            update_normal_form = Normal_User_Update_Form(requests.POST, requests.FILES ,instance=user.normal_user)

            if update_normal_form.is_valid() and update_normal_form.is_valid():
                  updated_user = update_user_form.save()
                  normal_user = update_normal_form.save(commit=False)
                  normal_user.user= updated_user
                  normal_user.save()

                  return redirect("all_users")

      else:
            update_user_form = User_Update_Form(instance=user)
            update_normal_form = Normal_User_Update_Form(instance=user.normal_user)
            

      context = {
            'update_normal_form':update_normal_form,
            'update_register_form':update_user_form
      }

      return render(requests,"ums/user/edit_profile.html",context)




######################
##### admin side  ####
######################


@login_required(login_url='/login')
# @admin_required()
def admin_dashboard(requests):

      # print(requests.user.normal_user.profile_pic)
      normal_users = User.objects.filter(is_staff = False).count()
      admin_users = User.objects.filter(is_staff=True).count()

      context = {
            'normal_user_count':normal_users,
            'admin_user_count':admin_users,
      }

      return render(requests,'ums/admin/admin_dashboard.html', context=context)


@login_required(login_url='/login')
def new_user(requests):
      if requests.POST:
            main_form  = Register_Form(requests.POST)
            normal_form = Normal_User_Form(requests.POST,requests.FILES)

            try:
                  user = User.objects.get(username= requests.POST['username'])
                  return HttpResponse("User already exists you moroon!!")
            except  User.DoesNotExist:
                  if main_form.is_valid() and normal_form.is_valid():
                        user = main_form.save()
                        normal_user = normal_form.save(commit=False)
                        normal_user.user= user
                        normal_user.save()


                        # username = main_form.cleaned_data.get('username')
                        # password = main_form.cleaned_data.get('password')

                        # user = authenticate(username=username,password=password)
                        # login(requests,user)
                        return redirect(new_user)
      else:
            main_form = Register_Form()
            normal_form = Normal_User_Form()
      context = {'main_form':main_form,'normal_form':normal_form}
                  
      return render(requests,"ums/admin/new_user.html",context)


@login_required(login_url='/login')
def edit_user(requests,pk):
      user = User.objects.get(pk = pk)
      # print(user)
      # print(pk)
      # register_form = User_Update_Form
      # normal_form =Normal_User_Update_Form

      print(user.normal_user.phone)
      
      if requests.POST:
                  
            update_user_form = User_Update_Form(data=requests.POST, instance=user)
            update_normal_form = Normal_User_Update_Form(requests.POST, requests.FILES ,instance=user.normal_user)

            if update_normal_form.is_valid() and update_normal_form.is_valid():
                  updated_user = update_user_form.save()
                  normal_user = update_normal_form.save(commit=False)
                  normal_user.user= updated_user
                  normal_user.save()

                  return redirect("all_users")

      else:
            update_user_form = User_Update_Form(instance=user)
            update_normal_form = Normal_User_Update_Form(instance=user.normal_user)
            

      context = {
            'update_normal_form':update_normal_form,
            'update_register_form':update_user_form
      }

      return render(requests,"ums/admin/edit_user.html",context)

def reset_password(request,pk):
      user = User.objects.get(pk=pk)
      new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
      
      if user:
            user.set_password(new_password)
            user.save()
            try:
                  send_mail(
                  'Password Reset',
                  f' Hi {user.first_name} <br> Your new Password for PDS is <srong>{new_password}</strong>',
                  'anilfyp@gmail.com',
                  [user.email],
                  fail_silently=False,)
            except:
                  return HttpResponse("Email Could not be sent.")

      return redirect("all_users")

def admin_profile(requests):
      user = requests.user
      return render(requests,"ums/admin/admin_profile.html",context={'user':user})


      
      








@login_required(login_url='/login')
def all_users(requests):
      users = User.objects.all()
      # for user in users:
            # print(user__.profile_pic)
      return render(requests,"ums/admin/manage_users.html",{'users':users})

@login_required(login_url='/login')
def delete_user(requests, pk):
      user = User.objects.get(pk=pk)
      print(pk)
      try:
            user.normal_user.profile_pic.delete()
      except:
            print("Admin")
      user.delete()
      return redirect('all_users')
      #url: /admin/usr/del/<id>

@login_required(login_url='/login')
def toggle_admin(requests,pk):
      user = User.objects.get(pk=pk)
      
      if user.is_staff:
            user.is_staff = False
            user.save()
      else:
            user.is_staff = True
            user.save()



@login_required(login_url='/login')
def toggle_block(requests,pk):
     
      user = User.objects.get(pk=pk)
     
      print(user)
      if user.is_active:
            user.is_active = False
            user.save()            # user.save()
            return redirect('all_users')

      else:
            user.is_active = True
            user.save()
            return redirect('all_users')
      return redirect('all_users')

def toggle_admin_role(requests,pk):
      user = User.objects.get(pk=pk)

      if user.is_staff:
            user.is_staff = False
            user.save()            # user.save()
            return redirect('all_users')

      else:
            user.is_staff = True
            user.save()
            return redirect('all_users')
      return redirect('all_users')

      



