from django.urls import path
from . import views

urlpatterns = [
    path('diagnose/', views.new_test, name="new_test")

]
