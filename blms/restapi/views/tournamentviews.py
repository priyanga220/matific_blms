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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    game_service = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, format=None):
        serializer = TournamentSerializer(
            self.game_service.loadTournaments(), many=True
        )
        return Response(serializer.data)


class TournamentGameList(APIView):
    game_service = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, pk: int, format=None):
        serializer = TournamentGameSerializer(
            self.game_service.loadTournamentGames(pk), many=True
        )
        return Response(serializer.data)


class TournamentScoreborad(APIView):
    game_service = GameService()

    @method_decorator(has_permission([UserRole.ADMIN, UserRole.COACH, UserRole.PLAYER]))
    def get(self, request, pk: int, format=None):

        score_board = self.game_service.loadScoreboard(pk)
        serializer = ScoreBoardSerializer(score_board, many=True)
        return Response(serializer.data)
