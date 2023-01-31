from rest_framework import viewsets

from ..serializers import ConseilSerializer
from ..modeles.conseil import Conseil

class ConseilViewset(viewsets.ModelViewSet):
   queryset = Conseil.objects.all()
   serializer_class = ConseilSerializer