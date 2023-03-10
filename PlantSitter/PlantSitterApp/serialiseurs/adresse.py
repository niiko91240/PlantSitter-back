from rest_framework import serializers

from ..modeles.adresse import Adresse

class AdresseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adresse
        fields = ('id','numVoie','rue','codePostal','ville','complement','coordonneeX','coordonneeY')