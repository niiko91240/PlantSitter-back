from django.contrib import admin
from .models import *

# Register your modeles here.
admin.site.register(Adresse)
admin.site.register(Conseil)
admin.site.register(Message)
admin.site.register(Plante)
admin.site.register(Publication)
admin.site.register(Utilisateur)