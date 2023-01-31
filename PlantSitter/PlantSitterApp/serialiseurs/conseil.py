from rest_framework import serializers

from ..modeles.conseil import Conseil

class ConseilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conseil
        fields = ('id','titre','description','image','idPlante')