from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from diagnose.models import Diagnose
from datetime import datetime
import random
from django.http import HttpResponse


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

    return render(requests,'ims/patients.html',context={'patients':all_patients})
    
@login_required(login_url="/login")
def single_patient(requests,pk):
    patient_details = Diagnose.objects.get(pk=pk)
    return render(requests,"ims/single_patient.html",context={"patient":patient_details})

@login_required(login_url='/login')
def stats(requests):
    # url: /usr/stats/
    # TODO
    return HttpResponse("Stats TO BE DONE")

def delete_patient_record(request,pk):
    info = Diagnose.objects.get(pk=pk)
    try:
        info.delete()
        return redirect("all_patients")
    except:
        print("Error Occured")
