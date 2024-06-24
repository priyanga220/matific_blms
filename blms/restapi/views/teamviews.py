from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator

from core.models import Player, UserRole
from ..serializers import TeamSerializer
from ..serializers import TeamViewSerializer
from ..serializers import PlayerSerializer
from ..serializers import TeamPlayerIdSerializer
from ..decorators import has_permission
from ..decorators import has_teampermission
from ..services import TeamService


class TeamList(APIView):
    teamservice = TeamService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH]))
    def get(self, request, format=None):
        serializer = TeamSerializer(self.teamservice.loadTeams(), many=True)
        return Response(serializer.data)


class TeamDetail(APIView):
    teamservice = TeamService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH]))
    @method_decorator(has_teampermission())
    def get(self, request, pk: int, format=None):
        serializer = TeamViewSerializer(data=self.teamservice.loadTeamView(pk))
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class PlayerListForTeam(APIView):
    teamservice = TeamService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH]))
    @method_decorator(has_teampermission())
    def get(self, request, pk: int, format=None):
        players: list[Player] = self.teamservice.loadPlayerListForTeam(pk)
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    @method_decorator(has_permission([UserRole.ADMIN]))
    def post(self, request, pk: int, format=None):
        serializer = TeamPlayerIdSerializer(request.data)
        player = self.teamservice.addPlayerToTheTeam(
            pk, serializer.data.get("player_id")
        )
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# get all players in the team who has average score in given percentile,
# if percetile not given, default to 90th and return all above 90
class PlayerListWithAveragePercentile(APIView):
    teamservice = TeamService()

    @method_decorator(has_permission([UserRole.COACH]))
    @method_decorator(has_teampermission())
    def get(self, request, pk: int, format=None):
        above_percentile = request.GET.get("percentile", 90)
        players: list[Player] = (
            self.teamservice.loadPlayerListForTeamAboveGivenPercentileScore(
                pk, above_percentile
            )
        )
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)
