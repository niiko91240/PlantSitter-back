from django.db import models
from .plante import Plante

class Conseil(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField(max_length=5)
    idPlante = models.ForeignKey(Plante, on_delete=models.CASCADE, related_name='plante')
