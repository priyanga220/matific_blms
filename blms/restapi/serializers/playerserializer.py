from rest_framework import serializers
from core.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "display_name", "height", "rank"]


class PlayerViewSerializer(serializers.Serializer):
    playerid = serializers.IntegerField()
    name = serializers.CharField()
    display_name = serializers.CharField()
    height = serializers.FloatField(required=False)
    average_score = serializers.FloatField(default=0)
    num_of_games_played = serializers.IntegerField(default=0)


class PlayerSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
