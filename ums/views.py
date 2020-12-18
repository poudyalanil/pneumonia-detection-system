from django.contrib.auth.backends import RemoteUserBackend
from django.db.models.aggregates import Count
from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .forms import Register_Form, Normal_User_Form, User_Update_Form, Normal_User_Update_Form, Issue_New_Ticket
from django.contrib.auth.models import User
from .models import Normal_User, User_Support_Ticket
from datetime import datetime
from django.core.mail import send_mail
# from .decorators import login_required

from django.contrib.auth.decorators import login_required
from .decorators import admin_required
import random
import string
import os
import requests
from . import mail_template
# Create your views here.


######################
##### general   ####
######################
def index(requests):
    # url: /
    return render(requests, 'ums/index.html')


def sign_in(requests):
    # url: /login
    if requests.POST:
        username = requests.POST['username']
        password = requests.POST['password']
        auth_user = authenticate(username=username, password=password)
        if auth_user:
            messages.success(requests, "Login Success")
            # requests.session['username'] = username
            login(requests, auth_user)

            if requests.user.is_staff:
                return redirect("admin_dashboard")
            else:

                return redirect('user_homepage')
            # TODO
        else:
            messages.error(requests, "Incorrect Credentials")

    return render(requests, 'ums/login.html')


@login_required(login_url='/login')
def log_out(requests):
    # url: /logout
    logout(requests)
    return redirect('homepage')


def request_user_register(requests):

    pass


######################
##### user side   ####
######################


@login_required(login_url='/login')
def user_support(requests):
    form = Issue_New_Ticket(data=requests.POST)
    current_user = requests.user.normal_user
    context = {}
    if requests.POST:
        if form.is_valid:
            main_form = form.save(commit=False)
            main_form.user = current_user
            main_form.save()
            title = f"PDS Support | {form.cleaned_data.get('title')}"
            message = f'''Hi {requests.user.first_name},<br> your ticket with title<strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> "{form.cleaned_data.get('title')}" </strong> has been issued at <strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">{datetime.now().strftime("%d %B, %Y")} </strong>. We are looking into issue, we will contact you once the issue has been resloved'''
            to = [requests.user.email]
            send_email(title, to, message)

            return redirect("user_support")
    else:
        context = {
            'form': Issue_New_Ticket(),
            'tickets': User_Support_Ticket.objects.filter(user=requests.user.normal_user)
        }

    return render(requests, 'ums/user/support.html', context)


@login_required(login_url='/login')
def support(requests):
    # url: /usr/support/
    # TODO
    pass


@login_required(login_url='/login')
def user_profile(requests):
    user = requests.user
    return render(requests, "ums/user/user_profile.html", context={'user': user})

    pass


@login_required(login_url='/login')
def edit_profile(requests):
    # url: /usr/profile/edt/<id>
    user = requests.user
    # print(user)
    # print(pk)
    # register_form = User_Update_Form
    # normal_form =Normal_User_Update_Form

    print(user.normal_user.phone)

    if requests.POST:

        update_user_form = User_Update_Form(data=requests.POST, instance=user)
        update_normal_form = Normal_User_Update_Form(
            requests.POST, requests.FILES, instance=user.normal_user)

        if update_normal_form.is_valid() and update_normal_form.is_valid():
            updated_user = update_user_form.save()
            normal_user = update_normal_form.save(commit=False)
            normal_user.user = updated_user
            normal_user.save()

            return redirect("all_users")

    else:
        update_user_form = User_Update_Form(instance=user)
        update_normal_form = Normal_User_Update_Form(instance=user.normal_user)

    context = {
        'update_normal_form': update_normal_form,
        'update_register_form': update_user_form
    }

    return render(requests, "ums/user/edit_profile.html", context)


######################
##### admin side  ####
######################


@login_required(login_url='/login')
# @admin_required()
def admin_dashboard(requests):

    # print(requests.user.normal_user.profile_pic)
    normal_users = User.objects.filter(is_staff=False).count()
    admin_users = User.objects.filter(is_staff=True).count()

    context = {
        'normal_user_count': normal_users,
        'admin_user_count': admin_users,
    }

    return render(requests, 'ums/admin/admin_dashboard.html', context=context)


@login_required(login_url='/login')
def new_user(requests):
    if requests.POST:
        main_form = Register_Form(requests.POST)
        normal_form = Normal_User_Form(requests.POST, requests.FILES)

        try:
            user = User.objects.get(username=requests.POST['username'])
            return HttpResponse("User already exists you moroon!!")
        except User.DoesNotExist:
            if main_form.is_valid() and normal_form.is_valid():
                user = main_form.save()
                normal_user = normal_form.save(commit=False)
                normal_user.user = user
                normal_user.save()

                # username = main_form.cleaned_data.get('username')
                # password = main_form.cleaned_data.get('password')

                # user = authenticate(username=username,password=password)
                # login(requests,user)
                return redirect(new_user)
    else:
        main_form = Register_Form()
        normal_form = Normal_User_Form()
    context = {'main_form': main_form, 'normal_form': normal_form}

    return render(requests, "ums/admin/new_user.html", context)


def request_new_user(requests):
    if requests.POST:
        main_form = Register_Form(requests.POST)
        normal_form = Normal_User_Form(requests.POST, requests.FILES)

        try:
            user = User.objects.get(username=requests.POST['username'])
            return HttpResponse("User already exists you moroon!!")
        except User.DoesNotExist:
            if main_form.is_valid() and normal_form.is_valid():
                user = main_form.save()
                normal_user = normal_form.save(commit=False)
                normal_user.user = user
                normal_user.is_request = True
                print("I am Here", user.email)
                user.is_active = False
                user.save()
                normal_user.save()
                to = main_form.cleaned_data.get('email')
                name = main_form.cleaned_data.get('first_name')

                title = "PDS Support| User Request Received"
                message = f'''Hi,<strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"> {name}</strong><br> your user request has been received. We will process the request as soon as possible'''

                send_email(to=to, title=title, message=message)

                # user = authenticate(username=username,password=password)
                # login(requests,user)
                return redirect('/')
    else:
        main_form = Register_Form()
        normal_form = Normal_User_Form()
    context = {'main_form': main_form, 'normal_form': normal_form}

    return render(requests, "ums/request.html", context)


@login_required(login_url='/login')
def edit_user(requests, pk):
    user = User.objects.get(pk=pk)
    # print(user)
    # print(pk)
    # register_form = User_Update_Form
    # normal_form =Normal_User_Update_Form

    print(user.normal_user.phone)

    if requests.POST:

        update_user_form = User_Update_Form(data=requests.POST, instance=user)
        update_normal_form = Normal_User_Update_Form(
            requests.POST, requests.FILES, instance=user.normal_user)

        if update_normal_form.is_valid() and update_normal_form.is_valid():
            updated_user = update_user_form.save()
            normal_user = update_normal_form.save(commit=False)
            normal_user.user = updated_user
            normal_user.save()

            return redirect("all_users")

    else:
        update_user_form = User_Update_Form(instance=user)
        update_normal_form = Normal_User_Update_Form(instance=user.normal_user)

    context = {
        'update_normal_form': update_normal_form,
        'update_register_form': update_user_form
    }

    return render(requests, "ums/admin/edit_user.html", context)


def reset_password(request, pk):
    user = User.objects.get(pk=pk)
    new_password = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))

    if user:
        user.set_password(new_password)
        user.save()
        message = f'''Hi, <strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">{user.first_name}</strong> your password for <strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">Pneumonia Detection System</strong> has been reset and your new password is
        
        <strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;"><u>{new_password}</u></strong> do not share this password with anyone. For further queries email <i>info@anilpoudyal.com.np</i>
        
        '''
        try:
            send_email(title="Password Reset",to=[user.email],message=message)
        except:
            return HttpResponse("Email Could not be sent.")

    return redirect("all_users")


def admin_profile(requests):
    user = requests.user
    return render(requests, "ums/admin/admin_profile.html", context={'user': user})


def support_tickets(requests):
    all_tickets = User_Support_Ticket.objects.all()
    return render(requests, 'ums/admin/support_tickets.html', {'tickets': all_tickets})


def close_ticket(requests, pk):
    ticket = User_Support_Ticket.objects.get(pk=pk)
    ticket.delete()
    send_email(message=f'''Dear user your issue['<strong style="font-family: 'Helvetica Neue',Helvetica,Arial,sans-serif; box-sizing: border-box; font-size: 14px; margin: 0;">{ticket.title}></strong>'] has been closed''',
               title=f"{ticket.title} has been closed | PDS Support", to=[ticket.user.user.email])

    return redirect('support_tickets')


def close_ticket_user(requests, pk):
    ticket = User_Support_Ticket.objects.get(pk=pk)
    ticket.delete()
    send_email(message=f"Dear user your issue[{ticket.title}] has been closed",
               title=f"{ticket.title} has been closed", to=ticket.user.user.email)

    return redirect('support_tickets')

# def search_user(requests,search_content):
#       if requests.POST:
#             search_input = requests.POST['search_input']

#             if search_input.contains('@')


@login_required(login_url='/login')
def all_users(requests):
    active_users = User.objects.filter(is_active=True)
    inactive_users = User.objects.filter(is_active=False)
    
    # normal_users = Normal_User.objects.filter(is_request=True).count()
    # print(normal_users)

    # for user in users:
    # print(user__.profile_pic)
    return render(requests, "ums/admin/manage_users.html", {'users': active_users, 'in_users': inactive_users})


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
    # url: /admin/usr/del/<id>


@login_required(login_url='/login')
def toggle_admin(requests, pk):
    user = User.objects.get(pk=pk)

    if user.is_staff:
        user.is_staff = False

    else:
        user.is_staff = True

    user.save()


@login_required(login_url='/login')
def toggle_block(requests, pk):

    user = User.objects.get(pk=pk)
    n_user = user.normal_user
    try:
        n_user.is_request = False
        n_user.save()
    except:
        print("Ramram")

    if user.is_active:
        user.is_active = False
        user.save()
        return redirect('all_users')

    else:
        user.is_active = True
        user.save()

        message = f"Hi {user.username} your account is now active you can perfom all the activites to the system"
        title = "Congratulations!! Your Account is now Active"
        to = user.email
        send_email(title, to, message)
        return redirect('all_users')

    # user.save()
    # return redirect('all_users')


def toggle_admin_role(requests, pk):
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


def send_email(title, to, message):

    formatted_message = mail_template.email(title,message)

    return requests.post(
		"https://api.eu.mailgun.net/v3/anilpoudyal.com.np/messages",
		auth=("api", "04eebd0cbfea5e49916810d84ae1ad96-e5da0167-c4002268"),
		data={"from": "fyp@anilpoudyal.com.np",
			"to": to,
			"subject": title,
			"text": message,
            'html':formatted_message,
            })


