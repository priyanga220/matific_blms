from rest_framework import serializers
from core.models import Tournament, Game


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = ["id", "name", "identifier", "mascot"]


class TournamentGameSerializer(serializers.ModelSerializer):
    teams = serializers.SerializerMethodField()
    game_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", source="date")

    def get_teams(self, obj):
        return (
            f"{(obj.gamestats.all()[0]).teamref} vs {(obj.gamestats.all()[1]).teamref}"
        )

    class Meta:
        model = Game
        fields = ["id", "game_level", "teams", "game_status", "game_time"]


class PlainGameSerilizer(serializers.Serializer):
    game_no = serializers.IntegerField()
    game_date_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    game_level = serializers.CharField()
    game_status = serializers.CharField()


class ScoreBoardSerializer(serializers.Serializer):
    game = PlainGameSerilizer()
    team1 = serializers.CharField()
    team1_score = serializers.IntegerField()
    team1_winner = serializers.CharField()
    team2 = serializers.CharField()
    team2_score = serializers.IntegerField()
    team2_winner = serializers.CharField()
