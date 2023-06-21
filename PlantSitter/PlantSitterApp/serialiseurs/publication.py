from rest_framework import serializers

from ..modeles.publication import Publication

class PublicationSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)
    nomAccepteur = serializers.CharField(source='get_nomAccepteur')
    nomCreateur = serializers.CharField(source='get_nomCreateur')

    class Meta:
        model = Publication
        fields = ('id','dateDebut','dateFin','heureDebut', 'heureFin','titre','description','image','plante','idCreateur','idAccepteur', 'nomAccepteur','nomCreateur')