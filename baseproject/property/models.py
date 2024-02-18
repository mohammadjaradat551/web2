from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class Property(models.Model):
    owner= models.ForeignKey(User, related_name='property_owner', on_delete= models.CASCADE)
    name= models.CharField(max_length=50, null= True, blank=True)
    description= models.CharField(max_length=5000, null= True, blank=True)
    price= models.IntegerField(default=0)
    main_image= models.ImageField(upload_to= 'property/')
    created_at= models.DateTimeField(default= timezone.now)
    place= models.ForeignKey('Place', related_name='property_place', on_delete=models.PROTECT)
    category= models.ForeignKey('Category', related_name='property_category', on_delete=models.PROTECT)
    
    #for create link same the name withot space(-)
    slug = models.SlugField(null= True, blank= True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        return super(Property, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs= {'slug':self.slug})
    
    
    
class Place(models.Model):
    name= models.CharField(max_length=50)
    image= models.ImageField(upload_to= 'places/')
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return self.name
        

class PropertyImages(models.Model):
    property= models.ForeignKey(Property, related_name= 'property_image', on_delete= models.CASCADE)
    image= models.ImageField(upload_to= 'propertyimages/')
    def __str__(self):
        return str(self.property)


class PropertyReview(models.Model):
    author= models.ForeignKey(User, related_name='property_reviewer', on_delete= models.CASCADE)
    property= models.ForeignKey(Property, related_name='property_review', on_delete= models.PROTECT)
    rate= models.IntegerField(default=0)
    feed_back= models.TextField(max_length= 10000)
    created_at= models.DateTimeField(default= timezone.now)

    def __str__(self) :
        return str(self.property)
    
COUNT= {
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    }

class PropertyBook(models.Model):
    user= models.ForeignKey(User, related_name='book_owner', on_delete= models.CASCADE)
    property= models.ForeignKey(Property, related_name='property_book', on_delete= models.PROTECT)
    date_from= models.DateTimeField(default= timezone.now)
    date_to= models.DateTimeField(default= timezone.now)
    guset= models.IntegerField(default=0, choices= COUNT, null= True, blank= True)
    children= models.IntegerField(default=0, choices= COUNT, null= True, blank= True)


    def __str__(self) :
        return str(self.property)
    



    
