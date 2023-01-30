from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register(r'utilisateur', UtilisateurViewSet)
router.register(r'adresse', AdresseViewset)


urlpatterns = [
    path('', include(router.urls)),
]