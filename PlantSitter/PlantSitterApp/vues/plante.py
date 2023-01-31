from rest_framework import viewsets

from ..serializers import PlanteSerializer
from ..modeles.plante import Plante

class PlanteViewset(viewsets.ModelViewSet):
   queryset = Plante.objects.all()
   serializer_class = PlanteSerializer