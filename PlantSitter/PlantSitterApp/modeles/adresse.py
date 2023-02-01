from django.db import models

class Adresse(models.Model):
    numVoie = models.IntegerField()
    rue = models.CharField(max_length=40)
    codePostal = models.IntegerField()
    ville = models.CharField(max_length=40)
    complement = models.CharField(max_length=40, null=True, blank=True)
    coordonneeX = models.FloatField(max_length=5)
    coordonneeY = models.FloatField(max_length=5)