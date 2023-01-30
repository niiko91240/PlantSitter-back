from django.db import models
from .adresse import Adresse

class Utilisateur(models.Model):
    login = models.CharField(max_length=30)
    mail = models.CharField(max_length=40)
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    mdp = models.CharField(max_length=30)
    isBotaniste = models.BooleanField()
    idAdresse = models.ForeignKey(Adresse, on_delete=models.CASCADE, related_name='adresse')