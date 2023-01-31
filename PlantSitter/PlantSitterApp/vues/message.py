from rest_framework import viewsets

from ..serializers import MessageSerializer
from ..modeles.message import Message

class MessageViewset(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   serializer_class = MessageSerializer