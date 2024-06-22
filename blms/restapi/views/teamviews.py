from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Player
from ..serializers import TeamSerializer
from ..serializers import TeamViewSerializer
from ..serializers import PlayerSerializer
from ..serializers import TeamPlayerIdSerializer

from ..services import TeamService


class TeamList(APIView):
    team_service = TeamService()

    def get(self, request, format=None):
        serializer = TeamSerializer(self.team_service.loadTeams(), many=True)
        return Response(serializer.data)


class TeamDetail(APIView):
    team_service = TeamService()

    def get(self, request, pk, format=None):
        serializer = TeamViewSerializer(data=self.team_service.loadTeamView(pk))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PlayerListForTeam(APIView):
    team_service = TeamService()

    def get(self, request, pk: int, format=None):
        players: list[Player] = self.team_service.loadPlayerListForTeam(pk)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def post(self, request, pk: int, format=None):
        serializer = TeamPlayerIdSerializer(request.data)
        player = self.team_service.addPlayerToTheTeam(
            pk, serializer.data.get("player_id")
        )
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# get all players in the team who has average score in given percentile,
# if percetile not given, default to 90th and return all above 90
class PlayerListWithAveragePercentile(APIView):
    team_service = TeamService()

    def get(self, request, pk: int, format=None):
        above_percentile = request.GET.get("percentile", 90)
        players: list[Player] = (
            self.team_service.loadPlayerListForTeamAboveGivenPercentileScore(
                pk, above_percentile
            )
        )
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
