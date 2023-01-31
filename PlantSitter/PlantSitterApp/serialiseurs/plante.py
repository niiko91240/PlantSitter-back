from rest_framework import serializers

from ..modeles.plante import Plante

class PlanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plante
        fields = ('id','nom','nomScientifique','image')