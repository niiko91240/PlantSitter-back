from rest_framework import serializers

from ..modeles.message import Message

class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('id','description','date','heure','image','idUtilisateur','idPublication')