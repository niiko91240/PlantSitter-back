from django.db import models

class Plante(models.Model):
    nom = models.CharField(max_length=60)
    nomScientifique = models.CharField(max_length=60)
    image = models.URLField()