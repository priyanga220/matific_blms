from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import TournamentSerializer
from ..serializers import TournamentGameSerializer
from ..serializers import ScoreBoardSerializer

from ..services import GameService


class TournamentList(APIView):
    game_service = GameService()

    def get(self, request, format=None):
        serializer = TournamentSerializer(
            self.game_service.loadTournaments(), many=True
        )
        return Response(serializer.data)


class TournamentGameList(APIView):
    game_service = GameService()

    def get(self, request, pk: int, format=None):
        serializer = TournamentGameSerializer(
            self.game_service.loadTournamentGames(pk), many=True
        )
        return Response(serializer.data)


class TournamentScoreborad(APIView):
    game_service = GameService()

    def get(self, request, pk: int, format=None):

        score_board = self.game_service.loadScoreboard(pk)
        serializer = ScoreBoardSerializer(score_board, many=True)
        return Response(serializer.data)
