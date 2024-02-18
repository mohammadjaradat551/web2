from django.shortcuts import render
from .filters import PropertyFilter 
from django.views.generic import  DetailView
from django_filters.views import FilterView
from .models import Property

# Create your views here.
class PropertyList(FilterView):
    model = Property
    paginate_by= 2

    #filter
    filterset_class= PropertyFilter
    template_name= 'Property/Property_List.html'

class PropertyDetail(DetailView):
    model = Property

