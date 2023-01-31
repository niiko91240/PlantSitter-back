from rest_framework import serializers

from ..modeles.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ('id','dateDebut','dateFin','titre','description','image','plante','idCreateur','idAccepteur')