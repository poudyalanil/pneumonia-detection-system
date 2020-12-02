from ums.views import admin_dashboard, close_ticket
from django.urls import path
from . import views

urlpatterns = [


    path('usr/home', views.user_homepage, name="user_homepage"),
    path('usr/patients', views.all_patients, name='all_patients'),
    path('usr/stats', views.stats, name='stats'),


]
