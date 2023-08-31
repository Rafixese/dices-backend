from django.db import IntegrityError
from rest_framework import viewsets
from .models import PlayerModel, GameModel
from .serializers import PlayerModelSerlializer, GameModelSerializer
from guardian.shortcuts import assign_perm, get_objects_for_user
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class PlayerModelViewSet(viewsets.ModelViewSet):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerModelSerlializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            playermodel_obj = super().create(request, *args, **kwargs)
            assign_perm('view_playermodel', request.user, playermodel_obj.data.serializer.instance)
            return playermodel_obj
        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).filter(
            pk__in=get_objects_for_user(self.request.user, 'view_playermodel', klass=PlayerModel)
        )


class GameModelViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all()
    serializer_class = GameModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            gamemodel_obj = super().create(request, *args, **kwargs)
            assign_perm('view_gamemodel', request.user, gamemodel_obj.data.serializer.instance)
            return gamemodel_obj
        except IntegrityError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).filter(
            pk__in=get_objects_for_user(self.request.user, 'view_gamemodel', klass=GameModel)
        )
