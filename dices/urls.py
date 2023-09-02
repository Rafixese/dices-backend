from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PlayerModelViewSet, GameModelViewSet, GameColModelViewSet

router = routers.DefaultRouter()
router.register('player', PlayerModelViewSet)
router.register('game', GameModelViewSet)
router.register(r'game/(?P<game_id>[0-9]+)/gamecol', GameColModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]