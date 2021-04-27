from django.db import models
from cloudinary.models import CloudinaryField

class Tags(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Category(models.Model):
    category =  models.CharField(max_length=255)

    def __str__(self):
        return self.category



class Blog(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255,default=' ',null=False,blank=False)
    tag =  models.ManyToManyField(Tags)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=200,default=' ')
    content= models.TextField(blank=True)
    feature_image = CloudinaryField(null=True,blank=True)
    



