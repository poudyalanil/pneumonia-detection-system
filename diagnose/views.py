from django.http import response
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from .forms import New_Test, Update_Patient_info
from django.views.decorators.csrf import csrf_exempt
from diagnose.models import Diagnose
import os
import time
from django.contrib import messages



BASE_API_URL = 'http://api.fyp.anilpoudyal.com.np'

# BASE_API_URL = 'http://127.0.0.1:5000/'


@csrf_exempt
def new_test(request):

    if request.POST:
        new_test_form = New_Test(request.POST, request.FILES)
        if new_test_form.is_valid:
            new_test_form.save()
            # x_ray_image = new_test_form.cleaned_data["x_ray_image"]
            this_data = Diagnose.objects.last()
            
            try:
                image_url = this_data.x_ray_image.url
                print(image_url)
                content = upload_image(image_url).json()
                analysed_image = content['analysed_image']
                affected_percentage = content['affected_percentage']
                this_data.analysed_image = analysed_image
                this_data.affected_percentage = affected_percentage
                this_data.save()
                messages.success(request, "Success: Test Carried Out Successfully")
                return redirect("single_patient",pk=this_data.id)

            except:
                this_data.delete()

            # print(response)
        messages.error(request, "Error: Unable to Process")
        return redirect("new_test")
    else:
        new_test_form = New_Test()
        context = {
            "form": new_test_form
        }

        return render(request, 'diagnose/new_test.html', context)

@csrf_exempt
def update_patient_records(request,pk):
    patient = Diagnose.objects.get(pk=pk)

    if request.POST:
        update_form = Update_Patient_info(data = request.POST,instance = patient)

        if update_form.is_valid:
            update_form.save()
            return redirect("/usr/patients")
    else:
        update_form = Update_Patient_info(instance=patient)

    context = {'form':update_form}

    return render(request,'diagnose/new_test.html',context=context)   

def check_api_call(base_url):
    response = requests.get(base_url)
    return response.json()




def upload_image(image):
    image_file = {'file': image}
    response = requests.post(
        url=BASE_API_URL+"upload-image", data=image_file)

    return response
