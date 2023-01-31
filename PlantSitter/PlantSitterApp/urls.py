from rest_framework import routers
from django.urls import include, path
from .views import *

router = routers.DefaultRouter()
router.register(r'utilisateur', UtilisateurViewSet)
router.register(r'adresse', AdresseViewset)
router.register(r'conseil', ConseilViewset)
router.register(r'message', MessageViewset)
router.register(r'plante', PlanteViewset)
router.register(r'publication', PublicationViewset)


urlpatterns = [
    path('', include(router.urls)),
]