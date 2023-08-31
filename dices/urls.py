from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PlayerModelViewSet, GameModelViewSet

router = routers.DefaultRouter()
router.register('player', PlayerModelViewSet)
router.register('game', GameModelViewSet)
# router.register('gamecol', GameColModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]