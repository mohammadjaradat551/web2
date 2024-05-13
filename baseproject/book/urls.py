from django.urls import path
from .views import *
from .api_views import *



app_name = 'book'

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('<slug:slug>', BookDetail.as_view(), name='book_detail'),

    #Api
    path('api/list/', BookApiList.as_view(), name='bookApiList'),
    path('api/list/<int:pk>', BookApiDetail.as_view(), name='bookApiDetail'),


]