from .models import Property
from .serializers import PropertySerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated


class PropertyApiList(ListCreateAPIView):
    queryset= Property.objects.all()
    serializer_class= PropertySerializers
    permission_classes = [IsAuthenticated]



class PropertyApiDetail(RetrieveUpdateDestroyAPIView):
    queryset= Property.objects.all()
    serializer_class= PropertySerializers
    permission_classes = [IsAuthenticated]
