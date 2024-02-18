from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author= models.ForeignKey(User, related_name='post_author', on_delete= models.CASCADE)
    title= models.CharField(max_length=100, null= True, blank=True)
    description= models.CharField(max_length=5000, null= True, blank=True)
    image= models.ImageField(upload_to= 'post/')
    created_at= models.DateTimeField(default= timezone.now)
    category= models.ForeignKey('Category', related_name='post_category', on_delete= models.PROTECT)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name= models.CharField(max_length=50, null= True, blank=True)
    
    def __str__(self):
        return self.name