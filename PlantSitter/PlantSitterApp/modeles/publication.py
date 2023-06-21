from django.db import models
from .plante import Plante
from .utilisateur import Utilisateur

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Publication(models.Model):
    dateDebut = models.DateField()
    dateFin = models.DateField()
    heureDebut = models.TimeField(null=True, blank=True)
    heureFin = models.TimeField(null=True, blank=True)
    titre = models.CharField(max_length=60)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    plante = models.ManyToManyField(Plante, related_name='plantes')
    idCreateur = models.ForeignKey(Utilisateur, related_name='createur', on_delete=models.CASCADE, blank=True, null=True)
    idAccepteur = models.ForeignKey(Utilisateur, related_name='accepteur', on_delete=models.CASCADE, blank=True, null=True)

    @property
    def get_nomAccepteur(self):
            "Returns the person's full name."
            if self.idAccepteur is not None:
                return self.idAccepteur.prenom + ' ' + self.idAccepteur.nom
            else:
                return "Demande en attente d'acceptation."

    @property
    def get_nomCreateur(self):
        "Returns the person's full name."
        if self.idCreateur is not None:
            return self.idCreateur.prenom + ' ' + self.idCreateur.nom
        else:
            return ""



