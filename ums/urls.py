from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="homepage"),
    path('login',views.sign_in, name="sign_in"),
    path('home',views.user_homepage, name="user_homepage"),
]

