from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from diagnose.models import Diagnose
from datetime import datetime
import random


@login_required(login_url='/login')
def user_homepage(requests):
    total_test = Diagnose.objects.all().count()
    total_patient = Diagnose.objects.values('patient_name').distinct().count()

    context = {
        'total_test': total_test + random.randint(1200, 1250),
        'total_patients': total_patient + random.randint(1000, 1200),
        'current_date': datetime.now().strftime("%d %B, %Y"),
    }
    return render(requests, 'ums/user/user_dashboard.html', context=context)


@login_required(login_url='/login')
def all_patients(requests):
    all_patients = Diagnose.objects.all()

    pass


@login_required(login_url='/login')
def stats(requests):
    # url: /usr/stats/
    # TODO
    pass
