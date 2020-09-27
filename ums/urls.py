from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="homepage"),
    path('logout',views.logout,name='logout'),
    path('login',views.sign_in, name="sign_in"),

    
    path('usr/home',views.user_homepage, name="user_homepage"),
    path('usr/patients',views.all_patients,name='all_patients'),
    path('usr/new',views.new_test,name='new_test'),
    path('usr/stats',views.stats,name='stats'),
    path('usr/support',views.support,name='support'),
    path('usr/profile/<str:username>',views.user_profile,name='user_profile'),
    path('usr/profile/edit/<str:username>',views.edit_profile,name='edit_profile')



]

