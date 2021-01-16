from django.db import models
from datetime import datetime
from django.db.models.fields import DateField

date = datetime.now().strftime("%d %B, %Y")

class Diagnose(models.Model):
   
    test_date = DateField(auto_now=True)
    patient_name = models.CharField(max_length=220,verbose_name="Full Name")
    patient_country = models.CharField(max_length=220,verbose_name="Country")
    patient_city = models.CharField(max_length=220,verbose_name="City")
    patient_phone = models.CharField(max_length=20,default="",verbose_name="Phone Number")
    patient_email = models.EmailField(max_length=50,blank=True,default="",verbose_name="Email Address")
    x_ray_image = models.ImageField(null=False, blank=False, verbose_name="X-Ray Image")
    # after analysing image the api hosts the image to imgur and sends back url of the image
    analysed_image = models.CharField(max_length=2083, default="")
    affected_percentage = models.CharField(max_length=50)
