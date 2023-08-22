from django.contrib import admin
from django.db.models import ManyToOneRel

from dices.models import PlayerModel


@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlayerModel._meta.get_fields() if not isinstance(field, ManyToOneRel)]
