from django.db import models
from datetime import datetime


class Diagnose(models.Model):
    test_date = datetime.now().strftime("%d %B, %Y")
    patient_name = models.CharField(max_length=220)
    patient_country = models.CharField(max_length=220)
    patient_city = models.CharField(max_length=220)
    x_ray_image = models.ImageField(null=False, blank=False)
    # after analysing image the api hosts the image to imgur and sends back url of the image
    analysed_image = models.CharField(max_length=2083, default="")
    affected_percentage = models.CharField(max_length=50)
