from django.urls import path
from .views import PostList, PostDetail, PostByCategory
from .api_views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name= 'post_list'),
    path('<slug:slug>', PostDetail.as_view(), name= 'post_detail'),
    
    path('category/<str:slug>', PostByCategory.as_view(), name='post_by_category'),

    #api
    path('api/list/', post_list_api, name='api_list'),
    path('api/list/<int:id>', post_detial_api, name='post_detialize'),
    path('api/list/filter/<str:query>', post_search_api, name='post_search_api'),  

]