from django.http import HttpResponse
from rest_framework import viewsets, status

from ..serializers import PublicationSerializer
from ..modeles.publication import Publication
from ..modeles.utilisateur import Utilisateur

from rest_framework.parsers import MultiPartParser, FormParser

class PublicationViewset(viewsets.ModelViewSet):
   queryset = Publication.objects.all()
   serializer_class = PublicationSerializer

   def create(self, request, *args, **kwargs):
      dateDebut = request.data['dateDebut']
      dateFin = request.data['dateFin']
      heureDebut = request.data['heureDebut']
      heureFin = request.data['heureFin']
      titre = request.data['titre']
      description = request.data['description']
      image = request.data['image']
      Createur = Utilisateur.objects.get(id=request.data['idCreateur'])

      publication = Publication(
         dateDebut=dateDebut,
         dateFin=dateFin,
         heureDebut=heureDebut,
         heureFin=heureFin,
         titre=titre,
         description=description,
         idCreateur=Createur,
      )

      publication.image = image
      publication.save()
      #plantes = request.data['plante']
      plantes = request.POST.getlist('plante')
      for plante in plantes:
         plante = plante.split(',')
         for plant in plante:
            publication.plante.add(int(plant))
      return HttpResponse(status=201)