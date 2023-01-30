from django.db import models
from .plante import Plante
from .utilisateur import Utilisateur

class Publication(models.Model):
    dateDebut = models.DateField()
    datefin = models.DateField()
    titre = models.CharField(max_length=60)
    description = models.TextField()
    image = models.FileField()
    models.ManyToManyField(Plante, related_name='plantes')
    idCreateur = models.ForeignKey(Utilisateur, related_name='createur', on_delete=models.CASCADE,)
    idAccepteur = models.ForeignKey(Utilisateur, related_name='accepteur', on_delete=models.CASCADE,)

