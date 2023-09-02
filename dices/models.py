from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class GameModel(models.Model):
    game_name = models.CharField(max_length=100, default=f'Game {datetime.now().strftime("%Y-%m-%d %H:%M")}')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='GameModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.id}#{self.game_name}'


class PlayerModel(models.Model):
    player_name = models.CharField(max_length=100, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='PlayerModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['player_name', 'created_by']

    def __str__(self):
        return f'{self.id}#{self.player_name}'


class GameColModel(models.Model):
    player_fk = models.ForeignKey(PlayerModel, on_delete=models.PROTECT, related_name='GameColModels')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='GameColModels')
    game_fk = models.ForeignKey(GameModel, on_delete=models.CASCADE, related_name='GameColModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    field_1 = models.IntegerField(default=None, null=True)
    field_2 = models.IntegerField(default=None, null=True)
    field_3 = models.IntegerField(default=None, null=True)
    field_4 = models.IntegerField(default=None, null=True)
    field_5 = models.IntegerField(default=None, null=True)
    field_6 = models.IntegerField(default=None, null=True)

    three_of_kind = models.IntegerField(default=None, null=True)
    four_of_kind = models.IntegerField(default=None, null=True)
    full_house = models.IntegerField(default=None, null=True)
    small_flush = models.IntegerField(default=None, null=True)
    big_flush = models.IntegerField(default=None, null=True)
    general = models.IntegerField(default=None, null=True)
    chance = models.IntegerField(default=None, null=True)

    class Meta:
        unique_together = ['game_fk', 'player_fk']

    @classmethod
    def __get_safe_value(cls, value):
        return value if value is not None else 0

    def has_bonus(self):
        return self.get_part_score_top_table_fields() >= 63

    def get_bonus(self):
        return 35 if self.has_bonus() else 0

    def get_part_score_top_table_fields(self):
        return self.__get_safe_value(self.field_1) + self.__get_safe_value(self.field_2) + self.__get_safe_value(
            self.field_3) + self.__get_safe_value(self.field_4) + self.__get_safe_value(
            self.field_5) + self.__get_safe_value(self.field_6)

    def get_part_score_top_table(self):
        return self.get_part_score_top_table_fields() + self.get_bonus()

    def get_part_score_bottom_table(self):
        return self.__get_safe_value(self.three_of_kind) + self.__get_safe_value(
            self.four_of_kind) + self.__get_safe_value(self.full_house) + self.__get_safe_value(
            self.small_flush) + self.__get_safe_value(self.big_flush) + self.__get_safe_value(
            self.general) + self.__get_safe_value(self.chance)

    def get_score(self):
        return self.get_part_score_top_table() + self.get_part_score_bottom_table()

    def __str__(self):
        return f'{self.id}#{self.game_fk}#{self.player_fk}'
