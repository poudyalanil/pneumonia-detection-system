from django.urls import  path
from . import views

urlpatterns = [
    path('', views.blog_index,name='blog_home'),
    path('/new',views.new_blog,name="new_blog"),
    path('/edit/<str:title>',views.edit_blog,name="edit_blog"),
    path('/read/<str:title>',views.read_blog,name="read_blog"),
    path('/new/tag',views.new_tag,name="new_tag"),
    path('/new/category',views.new_category,name="new_category"),
]