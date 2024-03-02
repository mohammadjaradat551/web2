from .models import Property
from .serializers import PropertySerializers
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PropertyApiList(ListAPIView):
    queryset= Property.objects.all()
    serializer_class= PropertySerializers



class PropertyApiDetail(RetrieveAPIView):
    queryset= Property.objects.all()
    serializer_class= PropertySerializers