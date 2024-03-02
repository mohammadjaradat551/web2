from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

class some_model_admin(SummernoteModelAdmin): # instead of model admin
    summernote_fields = '__all__' # use Summernote for all fields
    list_display= ['name', 'price', 'get_avg_rating', 'check_availability']
# Register your models here.
admin.site.register(Property, some_model_admin)

admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
admin.site.register(Place)
admin.site.register(Category)
class PropertyBookAdmin(admin.ModelAdmin):
    list_display=['property', 'available']
admin.site.register(PropertyBook, PropertyBookAdmin)
