from django.db import models

class Tags(models.Model):
    tag = models.CharField(max_length=255)

class Category(models.Model):
    category =  models.CharField(max_length=255)


class Blog(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255,default=' ',null=False,blank=False)
    tag =  models.ManyToManyField(Tags)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=200,default=' ')
    


