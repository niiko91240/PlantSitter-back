from django.db import models
from .plante import Plante
from .utilisateur import Utilisateur

class Publication(models.Model):
    dateDebut = models.DateField()
    dateFin = models.DateField()
    heureDebut = models.TimeField(null=True, blank=True)
    heureFin = models.TimeField(null=True, blank=True)
    titre = models.CharField(max_length=60)
    description = models.TextField()
    image = models.URLField()
    plante = models.ManyToManyField(Plante, related_name='plantes')
    idCreateur = models.ForeignKey(Utilisateur, related_name='createur', on_delete=models.CASCADE,)
    idAccepteur = models.ForeignKey(Utilisateur, related_name='accepteur', on_delete=models.CASCADE,)

