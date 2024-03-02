from django.urls import path
from .views import *
from .api_views import *



app_name = 'property'

urlpatterns = [
    path('', PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', PropertyDetail.as_view(), name='property_detail'),

    #Api
    path('api/list/', PropertyApiList.as_view(), name='PropertyApiList'),
    path('api/list/<int:pk>', PropertyApiDetail.as_view(), name='PropertyApiDetail'),


]