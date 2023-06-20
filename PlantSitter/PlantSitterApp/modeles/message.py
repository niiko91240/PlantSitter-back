from django.db import models
from .utilisateur import Utilisateur
from .publication import Publication

class Message(models.Model):
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    heure = models.TimeField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    idsrc = models.ForeignKey(Utilisateur, related_name='utsource', on_delete=models.CASCADE, null=True, blank=True)
    idDest = models.ForeignKey(Utilisateur, related_name='utdest', on_delete=models.CASCADE, blank=True, null=True)
    idPublication = models.ForeignKey(Publication, related_name='publication', on_delete=models.CASCADE,)

