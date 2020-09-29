from django.shortcuts import  redirect, render
from django.http import  HttpResponse

def admin_required(view_func):
    pass
    # def wrapper_func(request,*args,**kwrgs):
    #     if request.user.is_superuser:
    #         return view_func(request, *args, **kwrgs)
    #     else:
    #         return redirect("/usr/home")
    
    # return wrapper_func


