from rest_framework import viewsets
from django.http import HttpResponse
from rest_framework.response import Response

from ..serializers import UtilisateurSerializer
from ..modeles.utilisateur import Utilisateur

class UtilisateurViewSet(viewsets.ModelViewSet):
   queryset = Utilisateur.objects.all()
   serializer_class = UtilisateurSerializer

   def create(self, request, *args, **kwargs):
      mail = request.data['id']
      mdp = request.data['mdp']
      try:
         utilisateur = Utilisateur.objects.get(login=mail, mdp=mdp)
         return HttpResponse(utilisateur.id,status=201)
      except:
         return HttpResponse(status=400)
