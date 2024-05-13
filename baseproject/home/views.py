from django.shortcuts import render
from book.models import *
from django.db.models import Q, Count
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    categories= Category.objects.all()
    books= Book.objects.filter(
        Q(category__name= 'romantic') | Q(category__name= 'action'))[:4]
    
    
    context= {
        'publishers': Publisher.objects.all().annotate(book_count= Count('book_publisher')),
        'categories': categories,
        'customers': User.objects.all().count(),
        'books':books
    }
    return render(request, 'home/home_list.html', context)


def home_search(request):
    name = request.GET.get('name')
    publisher = request.GET.get('publisher')

    result= Book.objects.filter(
        Q(name__icontains=name) & Q(publisher__name__icontains= publisher)
    )
    

    return render(request, 'home/home_search.html', {'result':result})

def FilterByCategory(request, category):
    name_of_category = Category.objects.get(name=category)
    result= Book.objects.filter(category__name__icontains= name_of_category)
    return render(request, 'home/home_search.html', {'result':result})


def FilterByPublisher(request, publisher):
    publisher= publisher.objects.get(name=publisher)
    result= Book.objects.filter(publisher__name= publisher)
    return render(request, 'home/home_search.html', {'result':result})
    

        
    
