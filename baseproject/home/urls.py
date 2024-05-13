from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('search/', home_search, name='home_search'),
    path('category/<slug:category>', FilterByCategory, name='category_filter'),
    path('publisher/<slug:publisher>', FilterByPublisher, name='publisher_filter'),


]