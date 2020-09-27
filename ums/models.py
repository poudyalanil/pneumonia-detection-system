from django.db import models
from django.contrib.auth.models import User


class Normal_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #dob = models.DateField()
    phone = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20, default="Nepal")
    


    def __str__(self):
        return self.user.username
