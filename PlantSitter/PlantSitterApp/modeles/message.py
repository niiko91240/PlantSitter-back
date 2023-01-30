from django.db import models
from .utilisateur import Utilisateur
from .publication import Publication

class Message(models.Model):
    description = models.TextField()
    date = models.DateField()
    heure = models.DateField()
    image = models.FileField()
    idUtilisateur = models.ForeignKey(Utilisateur, related_name='utilisateur', on_delete=models.CASCADE,)
    idPublication = models.ForeignKey(Publication, related_name='publication', on_delete=models.CASCADE,)

