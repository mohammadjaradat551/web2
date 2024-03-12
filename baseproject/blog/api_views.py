from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts= Post.objects.all()
    data= PostSerializers(all_posts, many= True).data
    return Response({'data':data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detial_api(request, id):
    post= get_object_or_404(Post, id=id)#another way for handle the error if ı give the noe exist id
    data= PostSerializers(post).data
    return Response({'data':data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_search_api(request, query):
    post= Post.objects.filter(
        Q(title__icontains= query) |
        Q(description__icontains= query)
    )
    data= PostSerializers(post, many= True).data
    return Response({'data':data})
