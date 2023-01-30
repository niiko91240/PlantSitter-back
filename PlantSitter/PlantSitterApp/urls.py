from rest_framework import routers
from django.urls import include, path
from views import *
from . import views

router = routers.DefaultRouter()
router.register(r'utilisateur', UtilisateurViewSet)

urlpatterns = [
    path('', include(router.urls)),
]