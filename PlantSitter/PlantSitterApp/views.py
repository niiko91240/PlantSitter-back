from urllib.request import Request
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .vues.utilisateur import UtilisateurViewSet
from .vues.adresse import AdresseViewset
from .vues.message import MessageViewset
from .vues.plante import PlanteViewset
from .vues.publication import PublicationViewset
from .vues.conseil import ConseilViewset
from . import views
from .modeles.plante import Plante

def insert_api(request):
    text = '<p>Page du script d\insertion des données'
    # ---- INSERTION DES PLANTES ----
    result = requests.get("https://trefle.io/api/v1/plants?token=vOXF21k0p5h0HuIfLhzTtO1FTGvM2ZW4asvUNH8OYI4").json()
    text='<h1>Insertion des données de l\'api dans la base de données.</h1>'
    for plante in result['data']:
        InsertPlante = Plante()
        InsertPlante.nom = str(plante['common_name'])
        InsertPlante.nomScientifique = str(plante['scientific_name'])
        InsertPlante.image = str(plante['image_url'])
        InsertPlante.save()

    return HttpResponse(text)
@csrf_exempt
def update_publication(request, *args, **kwargs):
  print(request)
  return HttpResponse(status=201)


