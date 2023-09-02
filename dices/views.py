from django.db import IntegrityError
from rest_framework import viewsets
from .models import PlayerModel, GameModel, GameColModel
from .serializers import PlayerModelSerlializer, GameModelSerializer, GameColModelSerializer
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


class GameColModelViewSet(viewsets.ModelViewSet):
    queryset = GameColModel.objects.all()
    serializer_class = GameColModelSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            game_id = self.kwargs.get('game_id')
            game_col_data = request.data.copy()
            game_col_data['game_fk'] = game_id

            if not self.request.user.has_perm('view_gamemodel', GameModel.objects.get(pk=game_id)):
                raise PermissionError(f'User has no permission to game id {game_id}')
            if not self.request.user.has_perm('view_playermodel', PlayerModel.objects.get(pk=game_col_data.get('player_fk'))):
                raise PermissionError(f'User has no permission to player id {game_col_data.get("player_fk")}')

            serializer = self.get_serializer(data=game_col_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            assign_perm('view_gamecolmodel', request.user, serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except (IntegrityError, PermissionError, GameModel.DoesNotExist, PlayerModel.DoesNotExist) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset).filter(
            game_fk__in=get_objects_for_user(self.request.user, 'view_gamemodel', klass=GameModel)).filter(game_fk__exact=self.request.parser_context['kwargs']['game_id']).filter(
            pk__in=get_objects_for_user(self.request.user, 'view_gamecolmodel', klass=GameColModel)
        )
