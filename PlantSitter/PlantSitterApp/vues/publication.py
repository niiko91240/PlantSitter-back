from rest_framework import viewsets

from ..serializers import PublicationSerializer
from ..modeles.publication import Publication

class PublicationViewset(viewsets.ModelViewSet):
   queryset = Publication.objects.all()
   serializer_class = PublicationSerializer