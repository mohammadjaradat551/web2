from django.shortcuts import render


from property.models import *
from blog.models import Post

from django.db.models import Q, Count
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    num_of_restaurant= Property.objects.filter(category__name= 'restaurant').count()
    num_of_hotels= Property.objects.filter(category__name= 'hotels').count()
    num_of_houses= Property.objects.filter(category__name= 'house').count()
    count_of_hotels_house= num_of_hotels + num_of_houses
    hotels_and_rooms= Property.objects.filter(
        Q(category__name= 'hotels') | Q(category__name= 'house')
    )[:4]
    restaurant= Property.objects.filter(category__name= 'restaurant')[:4]
    posts= Post.objects.all()[:4]

    context= {
        'places': Place.objects.all().annotate(property_count= Count('property_place')),
        'categories': Category.objects.all(),
        'customers': User.objects.all().count(),
        'num_of_places': Place.objects.all().count(),
        'num_of_restaurant': num_of_restaurant,
        'count_of_hotels_house':count_of_hotels_house,
        'hotels_and_rooms':hotels_and_rooms,
        'restaurants':restaurant,
        'posts': posts,
    }
    return render(request, 'home/home_list.html', context)


def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    result= Property.objects.filter(
        Q(name__icontains=name) & Q(place__name__icontains= place)
    )
    

    return render(request, 'home/home_search.html', {'result':result})

def FilterByCategory(request, category):
    name_of_category = Category.objects.get(name=category)
    result= Property.objects.filter(category__name__icontains= name_of_category)
    return render(request, 'home/home_search.html', {'result':result})


def FilterByPlace(request, place):
    place= Place.objects.get(name=place)
    result= Property.objects.filter(place__name= place)
    return render(request, 'home/home_search.html', {'result':result})
    

        
    
