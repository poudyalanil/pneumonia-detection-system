from ums.views import admin_dashboard
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="homepage"),
    path('logout',views.log_out,name='logout'),
    path('login',views.sign_in, name="sign_in"),

    path('usr/home',views.user_homepage, name="user_homepage"),
    path('usr/patients',views.all_patients,name='all_patients'),
    path('usr/new',views.new_test,name='new_test'),
    path('usr/stats',views.stats,name='stats'),
    path('usr/support',views.support,name='support'),
    path('usr/profile/<str:username>',views.user_profile,name='user_profile'),
    path('usr/profile/edit/<str:username>',views.edit_profile,name='edit_profile'),


    path('admin',views.admin_dashboard,name='admin_dashboard'),
    path('admin/new-usr',views.new_user,name="new_user"),
    path('admin/usr/del/<int:pk>',views.delete_user,name='delete_user'),
    path('admin/usr/edit/<int:pk>',views.edit_user,name='edit_user'),
    path('admin/mg-usr',views.all_users,name='all_users'),
    path('admin/usr/block/<int:pk>',views.toggle_block,name='toggle_block'),
    path('admin/usr/reset/<int:pk>',views.reset_password,name='reset_password'),

]

