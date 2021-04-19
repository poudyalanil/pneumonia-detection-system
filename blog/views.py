from django.shortcuts import render
from django.http import HttpResponse

def blog_index(request):
    return HttpResponse("Blog index")

def new_blog():
    return HttpResponse("TODO")

def edit_blog(title):
    return HttpResponse("TODO")

def read_blog(title):
    return HttpResponse("TODO")
    