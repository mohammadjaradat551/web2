from .models import Book
from .serializers import BookSerializers
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class BookApiList(ListCreateAPIView):
    queryset= Book.objects.all()
    serializer_class= BookSerializers
    permission_classes = [IsAuthenticated]



class BookApiDetail(RetrieveUpdateDestroyAPIView):
    queryset= Book.objects.all()
    serializer_class= BookSerializers
    permission_classes = [IsAuthenticated]
