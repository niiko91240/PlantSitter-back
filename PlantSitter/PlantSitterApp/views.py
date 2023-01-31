from django.shortcuts import render

from .models import *
from .vues.utilisateur import UtilisateurViewSet
from .vues.adresse import AdresseViewset
from .vues.message import MessageViewset
from .vues.plante import PlanteViewset
from .vues.publication import PublicationViewset
from .vues.conseil import ConseilViewset


