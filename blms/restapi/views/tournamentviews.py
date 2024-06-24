from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator

from ..serializers import TournamentSerializer
from ..serializers import TournamentGameSerializer
from ..serializers import ScoreBoardSerializer
from ..decorators import has_permission
from ..services import GameService
from core.models import UserRole


class TournamentList(APIView):
    gameservice = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, format=None):
        serializer = TournamentSerializer(self.gameservice.loadTournaments(), many=True)
        return Response(serializer.data)


class TournamentGameList(APIView):
    gameservice = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, pk: int, format=None):
        serializer = TournamentGameSerializer(
            self.gameservice.loadTournamentGames(pk), many=True
        )
        return Response(serializer.data)


class TournamentScoreborad(APIView):
    gameservice = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, pk: int, format=None):

        scoreboard = self.gameservice.loadScoreboard(pk)
        serializer = ScoreBoardSerializer(scoreboard, many=True)
        return Response(serializer.data)
