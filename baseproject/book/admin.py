from django.contrib import admin
from .models import *

from django_summernote.admin import SummernoteModelAdmin

class some_model_admin(SummernoteModelAdmin): # instead of model admin
    summernote_fields = '__all__' # use Summernote for all fields
    list_display= ['name', 'price', 'get_avg_rating', 'check_availability']
# Register your models here.
admin.site.register(Book, some_model_admin)

admin.site.register(BookImages)
admin.site.register(BookReview)
admin.site.register(Publisher)
admin.site.register(Category)
class bookBookAdmin(admin.ModelAdmin):
    list_display=['book', 'available']
admin.site.register(BorrowBook, bookBookAdmin)
