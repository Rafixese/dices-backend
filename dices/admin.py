from django.contrib import admin
from django.db.models import ManyToOneRel

from dices.models import PlayerModel, GameModel, GameColModel


@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlayerModel._meta.get_fields() if not isinstance(field, ManyToOneRel)]


@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GameModel._meta.get_fields() if not isinstance(field, ManyToOneRel)]


@admin.register(GameColModel)
class GameColModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GameColModel._meta.get_fields() if not isinstance(field, ManyToOneRel)]
