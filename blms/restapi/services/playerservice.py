from django.db.models import Avg
from django.http import Http404

from core.models import Player
from core.models import PlayerStat


class PlayerService:

    def loadPlayerView(self, player_id: int):
        player = self.get_object(player_id)
        played_games = PlayerStat.objects.filter(player_id=player_id)
        average = played_games.aggregate(Avg("score"))["score__avg"] or 0
        result = {
            "playerid": player.id,
            "name": player.name,
            "display_name": player.display_name,
            "height": player.height,
            "rank": player.rank,
            "num_of_games_played": len(played_games),
            "average_score": average,
        }
        return result

    def get_object(self, pk: int) -> Player:
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404
