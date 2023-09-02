from rest_framework import serializers
from .models import PlayerModel, GameModel, GameColModel


class PlayerModelSerlializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']


class GameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameModel
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']


class GameColModelSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField('get_score')
    score_top = serializers.SerializerMethodField('get_part_score_top_table')
    score_bottom = serializers.SerializerMethodField('get_part_score_bottom_table')

    class Meta:
        model = GameColModel
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    @classmethod
    def get_score(cls, obj: GameColModel):
        return obj.get_score()

    @classmethod
    def get_part_score_top_table(cls, obj: GameColModel):
        return obj.get_part_score_top_table()

    @classmethod
    def get_part_score_bottom_table(cls, obj: GameColModel):
        return obj.get_part_score_bottom_table()
