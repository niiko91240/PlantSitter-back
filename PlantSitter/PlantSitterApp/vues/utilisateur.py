from rest_framework import viewsets

from ..serializers import UtilisateurSerializer
from ..modeles.utilisateur import Utilisateur

class UtilisateurViewSet(viewsets.ModelViewSet):
   queryset = Utilisateur.objects.all()
   serializer_class = UtilisateurSerializer