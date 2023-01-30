from django.shortcuts import render
from rest_framework import viewsets

from serializers import *
from models import *

class UtilisateurViewSet(viewsets.ModelViewSet):
   queryset = Utilisateur.objects.all()
   serializer_class = UtilisateurSerializer
