from typing import Any
from django.shortcuts import  redirect

from .filters import PropertyFilter 
from django.views.generic import  DetailView
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from .models import Property
from .forms import PropertyBookForm

# Create your views here.
class PropertyList(FilterView):
    model = Property
    paginate_by= 3

    #filter
    filterset_class= PropertyFilter
    template_name= 'Property/Property_List.html'

class PropertyDetail(FormMixin, DetailView):
    model = Property
    form_class = PropertyBookForm
    

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        current_property= self.get_object()
        context['related_properties']=Property.objects.filter(
            category=self.get_object().category).exclude(id= current_property.id)[:3]
        return context
    
            

    def post(self, request, *args, **kwargs):
        form= self.get_form()
        if form.is_valid():
            my_form= form.save(commit=False)
            my_form.user = request.user
            my_form.property = self.get_object()
            # The get_object() method tries to find the object based on the URL
            # of the request, using the  slug
            my_form.save()
            return redirect('/')




