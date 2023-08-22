from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PlayerModelViewSet

router = routers.DefaultRouter()
router.register('player', PlayerModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]