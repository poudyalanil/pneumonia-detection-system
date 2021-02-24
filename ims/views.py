from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from diagnose.models import Diagnose
from datetime import datetime
import random
import json
from django.http import HttpResponse


@login_required(login_url='/login')
def user_homepage(requests):
    total_test = Diagnose.objects.all().count()
    total_patient = Diagnose.objects.values('patient_name').distinct().count()

    context = {
        'total_test': total_test,
        'total_patients': total_patient ,
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

    all_cities = Diagnose.objects.only('patient_city')
    in_city={}    
    return render(requests,"ims/stats.html")

@login_required(login_url='/login')
def get_chart_pie_data(request,*args,**kwrgs):

    all_cities = Diagnose.objects.only('patient_city')
    in_city={
    
    }
    city_data = []
    city_labels =[]

    response_data = {}
   
    for  d in all_cities:
        if d.patient_city in in_city:
            in_city[d.patient_city] +=1
        else:
            in_city[d.patient_city]=1
    


    response_data['pie_city_data']=list(in_city.values())
    response_data['pie_city_labels']=list(in_city.keys())
    keys  = in_city.keys()
    print(response_data)
    return JsonResponse(response_data)

@login_required(login_url='/login')
def get_chart_line_data(request,*args,**kwrgs):
    all_dates = Diagnose.objects.only('test_date')

    dates = {}
    response_data ={}

    for date in all_dates:
        if date.test_date in dates:
            dates[date.test_date]+=1
        else:
            dates[date.test_date]=1
    response_data['line_date_data']=list(dates.values())
    response_data['line_date_labels']=list(dates.keys())

    return JsonResponse(response_data)    


@login_required(login_url='/login')
def delete_patient_record(request,pk):
    info = Diagnose.objects.get(pk=pk)
    try:
        info.delete()
        return redirect("all_patients")
    except:
        print("Error Occured")
