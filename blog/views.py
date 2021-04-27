from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Create_New_Blog,Create_New_Category,Create_New_Tag
from .models import Blog,Tags,Category
from django.contrib.auth.decorators import login_required



def blog_index(request):
    #TODO  19th April
    all_blogs = Blog.objects.all()
    print(all_blogs)
    return render(request,"blog/index.html",context={"featured":all_blogs,"all_blogs":all_blogs})

@login_required(login_url='/login')
def new_blog(request):

    form = Create_New_Blog(request.POST,request.FILES)
    context = {}
    if request.POST:
        if form.is_valid():
            form.save()
            notify_me();
            notify_all_users();

            return redirect("new_blog")

            # return redirect
    else:
        context={
            'form':form
        }
    #TODO  21th April
    return render(request,"blog/new.html",context=context)

@login_required(login_url='/login')
def edit_blog(title):
    #TODO  21th April
    return HttpResponse("TODO")

def read_blog(title):
    #TODO  19th April
    return HttpResponse("TODO")

@login_required(login_url='/login')
def new_tag(request):
    form = Create_New_Tag(request.POST)
    context ={}

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("new_tag")

    else:
        context={
            'form':form
        }
    return render(request,"blog/new.html",context=context)
@login_required(login_url='/login')
def new_category(request):
    #TODO  19th April

    form = Create_New_Category(request.POST)
    context ={}

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("new_category")
    else:
        context={
            'form':form
        }
    return render(request,"blog/new.html",context=context)
@login_required(login_url='/login')
def notify_all_users():


    #TODO  21th April
    pass
@login_required(login_url='/login')
def notify_me():
    pass
