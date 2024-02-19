from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.

class Post(models.Model):
    author= models.ForeignKey(User, related_name='post_author', on_delete= models.CASCADE)
    title= models.CharField(max_length=100, null= True, blank=True)
    description= models.CharField(max_length=5000, null= True, blank=True)
    image= models.ImageField(upload_to= 'post/')
    created_at= models.DateTimeField(default= timezone.now)
    category= models.ForeignKey('Category', related_name='post_category', on_delete= models.PROTECT)
    slug = models.SlugField(null= True, blank= True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            return super(Post, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug':self.slug})
    
class Category(models.Model):
    name= models.CharField(max_length=50, null= True, blank=True)
    
    def __str__(self):
        return self.name