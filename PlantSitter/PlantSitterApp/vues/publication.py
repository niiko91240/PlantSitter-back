from django.http import HttpResponse
from rest_framework import viewsets, status

from ..serializers import PublicationSerializer
from ..modeles.publication import Publication
from rest_framework.parsers import MultiPartParser, FormParser

class PublicationViewset(viewsets.ModelViewSet):
   queryset = Publication.objects.all()
   serializer_class = PublicationSerializer
   parser_classes = (MultiPartParser, FormParser)

   def create(self, request, *args, **kwargs):
      dateDebut = request.data['dateDebut']
      dateFin = request.data['dateFin']
      heureDebut = request.data['heureDebut']
      heureFin = request.data['heureFin']
      titre = request.data['titre']
      description = request.data['description']
      image = request.data['image']
      idCreateur = request.data['idCreateur']
      idAccepteur = request.data['idAccepteur']
      idAccepteur = request.data['idAccepteur']
      publication = Publication(
         dateDebut=dateDebut,
         dateFin=dateFin,
         heureDebut=heureDebut,
         heureFin=heureFin,
         titre=titre,
         description=description,
      )
      publication.image = image
      publication.save()
      return HttpResponse(status=201)