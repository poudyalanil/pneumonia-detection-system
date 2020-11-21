from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def user_homepage(requests):
    # url: /usr/home
    # TODO
    return render(requests, 'ums/user/user_dashboard.html')


@login_required(login_url='/login')
def all_patients(requests):
    # url: /usr/patients/
    # TODO
    pass


@login_required(login_url='/login')
def new_test(requests):
    # url: /usr/new/
    # TODO
    pass


@login_required(login_url='/login')
def stats(requests):
    # url: /usr/stats/
    # TODO
    pass
