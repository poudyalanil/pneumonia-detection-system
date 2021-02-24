from ums.views import admin_dashboard, close_ticket
from django.urls import path
from . import views

urlpatterns = [


    path('usr/home', views.user_homepage, name="user_homepage"),
    path('usr/patients', views.all_patients, name='all_patients'),
    path('usr/stats', views.stats, name='stats'),
    path('usr/patients/<int:pk>', views.single_patient, name='single_patient'),
    path('usr/patients/del/<int:pk>', views.delete_patient_record, name='delete_record'),

    path('usr/charts/city/pie',views.get_chart_pie_data),
    path('usr/charts/date/line',views.get_chart_line_data),



]
