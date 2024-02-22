from django.db import models

# Create your models here.

class Home(models.Model):
    site_name= models.CharField(max_length= 50)
    logo= models.ImageField(upload_to= 'setting/')
    phone= models.CharField(max_length= 50)
    email= models.EmailField(max_length= 50)
    facebook_link= models.URLField(max_length = 200)
    twitter_link= models.URLField(max_length = 200)
    instagram_link= models.URLField(max_length = 200)

    def __str__(self):
        return self.site_name
