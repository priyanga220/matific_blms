from rest_framework import serializers
from core.models import Team
from .coachserializer import CoachReferenceSerializer


# Serilizer for team reference (id, name)
class TeamReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name"]


class TeamViewSerializer(serializers.Serializer):
    teamid = serializers.IntegerField()
    name = serializers.CharField()
    displayname = serializers.CharField()
    slogan = serializers.CharField(required=False)
    rank = serializers.IntegerField(required=False)
    average_score = serializers.FloatField(default=0, required=False)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "displayname", "slogan", "rank"]


class TeamSerializerFull(serializers.ModelSerializer):
    coach = CoachReferenceSerializer()

    class Meta:
        model = Team
        fields = "__all__"
        extra_fields = ["coach"]


class TeamPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamPlayerIdSerializer(serializers.Serializer):
    player_id = serializers.IntegerField()
