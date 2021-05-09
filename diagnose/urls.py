from django.urls import path
from . import views

urlpatterns = [
    path('diagnose/', views.new_test, name="new_test"),
    path('patient/edit/<int:pk>', views.update_patient_records, name="update_patient_record")

]
