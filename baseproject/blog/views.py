
from typing import Any


from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.db.models import Q


# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by= 4

    def get_queryset(self):
        search= self.request.GET.get('q', '')
        object_list= Post.objects.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )
        return object_list



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        current_post= self.get_object()
        context= super().get_context_data(**kwargs)
        context['categories']= Category.objects.all()
        context['recent_post']= Post.objects.all().exclude(id= current_post.id)[:3]
        return context

class PostByCategory(ListView):
    model = Post

    def get_queryset(self) :
        slug= self.kwargs['slug']
        object_list= Post.objects.filter(
            Q(category__name__icontains= slug)
        )
        return object_list

