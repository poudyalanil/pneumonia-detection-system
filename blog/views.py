from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Create_New_Blog,Create_New_Category,Create_New_Tag


def blog_index(request):
    #TODO  19th April
    return HttpResponse("Blog index")

def new_blog(request):

    form = Create_New_Blog(data=request.POST)
    context = {}
    if request.POST:
        if form.is_valid():
            form.save()
            notify_me();
            notify_all_users();

            # return redirect
    else:
        context={
            'form':form
        }
    #TODO  21th April
    return HttpResponse("TODO")

def edit_blog(title):
    #TODO  21th April
    return HttpResponse("TODO")

def read_blog(title):
    #TODO  19th April
    return HttpResponse("TODO")

def new_tag(request):
    form = Create_New_Tag()
    context ={}

    if request.POST:
        if form.is_valid():
            form.save()

    #TODO  19th April
    pass

def new_category(request):
    #TODO  19th April

    form = Create_New_Category()
    context ={}

    if request.POST:
        if form.is_valid():
            form.save()
    pass

def notify_all_users():


    #TODO  21th April
    pass

def notify_me():
    pass
