from django.db import models
from .plante import Plante

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Conseil(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    idPlante = models.ForeignKey(Plante, on_delete=models.CASCADE, related_name='plante')
