from django.db import models
from django.contrib.auth.models import User


class GameModel(models.Model):
    game_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='GameModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


class PlayerModel(models.Model):
    player_name = models.CharField(max_length=100, null=False, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='PlayerModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['player_name', 'created_by']


class GameColModel(models.Model):
    player_fk = models.ForeignKey(PlayerModel, on_delete=models.PROTECT, related_name='GameColModels')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='GameColModels')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    field_1 = models.IntegerField()
    field_2 = models.IntegerField()
    field_3 = models.IntegerField()
    field_4 = models.IntegerField()
    field_5 = models.IntegerField()
    field_6 = models.IntegerField()

    three_of_kind = models.IntegerField()
    four_of_kind = models.IntegerField()
    full_house = models.IntegerField()
    small_flush = models.IntegerField()
    big_flush = models.IntegerField()
    general = models.IntegerField()
    chance = models.IntegerField()

    def has_bonus(self):
        return self.field_1 + self.field_2 + self.field_3 + self.field_4 + self.field_5 + self.field_6 >= 63

    def get_bonus(self):
        return 35 if self.has_bonus() else 0

    def get_part_score_top_table(self):
        return self.field_1 + self.field_2 + self.field_3 + self.field_4 + \
            self.field_5 + self.field_6 + self.get_bonus()

    def get_part_score_bottom_table(self):
        return self.three_of_kind + self.four_of_kind + self.full_house + self.small_flush + \
            self.big_flush + self.general + self.chance

    def get_score(self):
        return self.get_part_score_top_table() + self.get_part_score_bottom_table()