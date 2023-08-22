from rest_framework import serializers
from .models import PlayerModel


class PlayerModelSerlializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']
