from django.urls import  path
from . import views

urlpatterns = [
    path('', views.blog_index,name='blog_home'),
    path('/new',views.new_blog,name="new_blog"),
    path('/edit/<slug:slug>',views.edit_blog,name="edit_blog"),
    
    path('/del/<slug:slug>',views.delete_blog,name="delete_blog"),

    path('/read/<slug:slug>',views.read_blog,name="read_blog"),
    path('/new/tag',views.new_tag,name="new_tag"),
    path('/new/category',views.new_category,name="new_category"),
]