from rest_framework import serializers

from ..modeles.utilisateur import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = ('id','login','mail','prenom','nom','mdp','isBotaniste','idAdresse')