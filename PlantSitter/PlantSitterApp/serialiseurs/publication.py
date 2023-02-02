from rest_framework import serializers

from ..modeles.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)

    class Meta:
        model = Publication
        fields = ('id','dateDebut','dateFin','heureDebut', 'heureFin','titre','description','image','plante','idCreateur','idAccepteur')