from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Normal_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #dob = models.DateField()
    phone = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20, default="Nepal")
    profile_pic= models.ImageField( null = True,blank =True)
    is_request =models.BooleanField(blank=True,default=False)

    def __str__(self):
        return self.user.username

class User_Support_Ticket(models.Model):
    user = models.ForeignKey(Normal_User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,null=True, blank=False)
    message = models.TextField()
    time = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title



    


