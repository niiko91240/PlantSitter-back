from rest_framework import viewsets

from ..serializers import AdresseSerializer
from ..modeles.adresse import Adresse

class AdresseViewset(viewsets.ModelViewSet):
   queryset = Adresse.objects.all()
   serializer_class = AdresseSerializer