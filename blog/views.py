from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Create_New_Blog,Create_New_Category,Create_New_Tag,Edit_Blog
from .models import Blog,Tags,Category
from django.contrib.auth.decorators import login_required
import datetime



def blog_index(request):
    #TODO  19th April
    blogs = Blog.objects.all().order_by('-last_updated')
    # print(all_blogs)
    return render(request,"blog/index.html",context={"featured":blogs})

@login_required(login_url='/login')
def new_blog(request):

    form = Create_New_Blog(request.POST,request.FILES)
    context = {}
    if request.POST:
        if form.is_valid():
            form.save()
            notify_all_users();

            return redirect("new_blog")
    else:
        context={
            'form':form
        }
    #TODO  21th April
    return render(request,"blog/new.html",context=context)

@login_required(login_url='/login')
def edit_blog(request,slug):
   
    blog = Blog.objects.get(slug=slug)

    if request.POST:
        update_form = Edit_Blog(data=request.POST,instance =blog)

        if update_form.is_valid():
            update_form.save()
            notify_all_users()
            return redirect('blog_home')
    else:
           update_form = Edit_Blog(instance =blog)
    
    context={"form":update_form}

    return render(request,'blog/new.html',context=context)


@login_required(login_url='/login')
def delete_blog(request,slug):
   
    blog = Blog.objects.get(slug=slug)

    if blog:
        blog.delete()
        return redirect("blog_home")

def read_blog(request,slug):
    #TODO  19th April
    blog = Blog.objects.get(slug=slug)
    category = blog.category
    recommended_blogs = Blog.objects.filter(category=category).exclude(slug=slug).order_by('-last_updated')[:3]


    return render(request,'blog/single_blog.html',context={'blog':blog,'recommend':recommended_blogs})

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

def notify_all_users():
    #TODO
    print("Hello World")


