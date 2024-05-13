
from django.shortcuts import  redirect
from .filters import BookFilter 
from django.views.generic import  DetailView
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from .models import Book
from .forms import *

# Create your views here.
class BookList(FilterView):
    model = Book
    paginate_by= 3

    #filter
    filterset_class= BookFilter
    template_name= 'book/book_List.html'



class BookDetail(FormMixin, DetailView):
    model = Book
    form_class = BorrowBookForm
    

    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        current_book= self.get_object()
        context['related_properties']=Book.objects.filter(
            category=self.get_object().category).exclude(id= current_book.id)[:3]
        return context
    
            

    def post(self, request, *args, **kwargs):
        form= self.get_form()
        if form.is_valid():
            my_form= form.save(commit=False)
            my_form.user = request.user
            my_form.book = self.get_object()
            # The get_object() method tries to find the object based on the URL
            # of the request, using the  slug
            my_form.save()
            return redirect('/')
        
        



