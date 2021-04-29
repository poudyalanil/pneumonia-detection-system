from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


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

    slug = models.SlugField(max_length=255,default=title,unique=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=200,default=' ',null=True,blank=True)
    content= models.TextField(blank=True)
    feature_image = CloudinaryField(null=True,blank=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.title) # set the slug explicitly
            super(Blog, self).save(*args, **kwargs) # call Django's save()
    



