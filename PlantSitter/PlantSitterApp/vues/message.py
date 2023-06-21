from rest_framework import viewsets

from ..serializers import MessageSerializer
from ..modeles.message import Message

class MessageViewset(viewsets.ModelViewSet):
   queryset = Message.objects.all()
   serializer_class = MessageSerializer

   def get_queryset(self):
      idPublication = self.request.GET.get('idPublication')
      if idPublication is not None:
         return Message.objects.filter(idPublication=idPublication)
      else:
         return Message.objects.all()